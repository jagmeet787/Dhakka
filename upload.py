import falcon

import io
import os
import shutil

from permissions import PermissionsResource
from database import database

from androwarn.warn.report.report import generate_report
from androwarn.warn.analysis.analysis import perform_analysis
from androwarn.warn.search.search import grab_application_package_name

from androguard.misc import AnalyzeAPK

class UploadResource(object):
    
    permissions_service = PermissionsResource()
    database_service = database()
    upload_directory_base = "./Files"

    def on_post(self, req, resp):
        print 'uploading file'
        print req
    	# save entry to the database
        id = self.database_service.inser_record("Processing")
        # create directory to store the file
        file_dir = self.upload_directory_base + "/" + str(id) + "/"
        os.makedirs(file_dir)
        # save the file
        apk = req.get_param('apk')
        file_path = file_dir + apk.filename
        raw = apk.file.read()
        open(file_path, 'wb').write(raw)
        # get permissions
        a, d, dx = AnalyzeAPK(file_path)
        permissions = self.permissions_service.getPermissions(a)
        print permissions
        # pass permissions to ml model
        # androwarn report generate in html
        package_name = grab_application_package_name(a)
        data = perform_analysis(file_path, a, d, dx, False)
        # 'Verbosity level (ESSENTIAL 1, ADVANCED 2, EXPERT 3) (default 1)'
        generate_report(package_name, data, 1, 'html', file_dir + 'index.html')
        # maldrolyzer report and send back in the body
        resp.body = "Done"
        resp.status = falcon.HTTP_201