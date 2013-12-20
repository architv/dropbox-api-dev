import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'uvoxyx3v827ogz1'
app_secret = 'dwbrnxvp243pfqz'

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
authorize_url = flow.start() #start - Allows user to authenticate your app 

# Have the user sign in and authorize this token
authorize_url = flow.start()
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code) #finish - Allows you to use the code that user give and authenticate your app

#The class that lets you make Dropbox API calls. You’ll need to obtain an OAuth 2 access token first. You can get an access token using either DropboxOAuth2Flow or DropboxOAuth2FlowNoRedirect.
client = dropbox.client.DropboxClient(access_token)
print 'linked account: ', client.account_info()

#Uploading file
f = open('/home/archit/Documents/Dropbox/dropbox-python-sdk-1.6/working-draft.txt')
response = client.put_file('/magnum-opus.txt', f) #put_file takes a path pointing to where we want the file, a file-like object to be uploaded there.
print "uploaded:", response

#metadata for folder
folder_metadata = client.metadata('/')
print "metadata:", folder_metadata

#downloading file
f, metadata = client.get_file_and_metadata('/magnum-opus.txt')
out = open('magnum-opus.txt', 'w')
out.write(f.read())
out.close()
print metadata #return metadata about the file
