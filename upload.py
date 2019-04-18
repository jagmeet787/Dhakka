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
    	# save entry to the database
        apk = req.get_param('apk')
        id = self.database_service.inser_record(apk.filename, "Processing")
        # create directory to store the file
        file_dir = self.upload_directory_base + "/" + str(id) + "/"
        os.makedirs(file_dir)
        # save the file
        file_path = file_dir + apk.filename
        raw = apk.file.read()
        open(file_path, 'wb').write(raw)
        resp.body = "Done"
        resp.status = falcon.HTTP_201