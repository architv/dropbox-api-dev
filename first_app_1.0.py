# -*- coding: utf-8 -*-
import webbrowser
import os
from configobj import ConfigObj
import dropbox

class DropboxApp:
    def __init__(self): #constructor       
        app_key = 'uvoxyx3v827ogz1'
        app_secret = 'dwbrnxvp243pfqz'
        access_type = "dropbox"
        TOKENS = './dropbox_token.txt'

        #first check if the user has already authenticated the app before
        try:
            token_file = open(TOKENS)
            token_key,token_secret = token_file.read().split('|')
            token_file.close()
            sess = dropbox.session.DropboxSession(app_key,app_secret,access_type )
            sess.set_token(token_key,token_secret)
            self.client = dropbox.client.DropboxClient(sess)
           
        #if the user is using the app for the first time, we'll have to authenticate the app first    
        except:
            session = dropbox.session.DropboxSession(app_key,app_secret,access_type)
            
            request_token = session.obtain_request_token()
     
            url = session.build_authorize_url(request_token)
            webbrowser.open_new_tab(url) 
            raw_input("Press enter to continue")
            access_token = session.obtain_access_token(request_token)
     
            self.client = dropbox.client.DropboxClient(session)

            #save the tokens so that the user doesn't have to authenticate again
            token_file = open(TOKENS,'w')
            token_file.write("%s|%s" % (access_token.key,access_token.secret) )
            token_file.close()

    def download_cont(self, folderName):
        fname = folderName
        folder_metadata = self.client.metadata('/' + fname)
        #print folder_metadata
        for path in [entry['path'] for entry in self.client.metadata('/' + fname)['contents'] if not entry['is_dir']]:
            name = os.path.basename(path)
            print 'Saving "%s"...' % name
            try:
                with open(name, 'wb') as out:
                    with self.client.get_file(path) as f:
                        out.write(f.read())
            except:
                print "error"
                
    def upload_cont(self, upload):
        bigFile = open(upload, 'rb')
        size = os.path.getsize(upload)
        uploader = self.client.get_chunked_uploader(bigFile, size)
        print "uploading:", size, "bytes"
        while uploader.offset < size:
            try:
                upload = uploader.upload_chunked()
            except rest.ErrorResponse, e:
                print "Error"
        uploader.finish('/bigFile.txt')
        print "File uploaded successfully"
        
if __name__ == "__main__":
    drop = DropboxApp()
    folderName = 'images'    
    drop.download_cont('./images')
    drop.upload_cont('file_to_be_uploaded.txt')
    
        
        
        



