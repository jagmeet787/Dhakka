import falcon
import io
import os
import shutil
from permissions import PermissionsResource
from warn.report.report import generate_report
from warn.analysis.analysis import perform_analysis
from androguard.misc import AnalyzeAPK

class UploadResource(object):
    permissionsService = PermissionsResource()
    def on_post(self, req, resp):
    	apk = req.get_param('apk')
    	raw = apk.file.read()
    	if apk.filename:
    		filename = apk.filename
    		open(filename, 'wb').write(raw)
    	# pass permissions to ml model
        # androwarn report generate in html
        a, d, dx = AnalyzeAPK(filename)
        permissions = permissionsService.getPermissions(a)
        package_name = grab_application_package_name(a)
        data = perform_analysis(filename, a, d, x, False)
        # 'Verbosity level (ESSENTIAL 1, ADVANCED 2, EXPERT 3) (default 1)'
        generate_report(package_name, data, 1, 'html', 'index.html')
        # maldrolyzer report and send back in the body
        resp.status = falcon.HTTP_201