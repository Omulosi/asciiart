Ascii Art
==========
A message board for displaying and sharing ascii art.

This application was developed on the Google App Engine platform.

To run this applicaton, you need to have the App Engine SDK for Python installed on your machine. Linux users can follow the steps listed below:
1. Download the App Engine SDK for Python.
2. Unzip the google_appengine_1.9.75.zip file that you downloaded, for example:
```
unzip google_appengine_1.9.75.zip
```
3. Add the google_appengine directory to your PATH:
```
export PATH=$PATH:DIRECTORY_PATH/google_appengine/
```
4. Ensure Python 2.7 is installed on your machine.

After completing this steps, you can clone this repo, cd into the project directory and run the following command to start a local server:
```
dev_appserver .
```

Note that the period stands for the current directory.

For more detailed instructions, check out the [Google Cloud](https://cloud.google.com/appengine/docs/standard/python/download) docs.

To read more about developing App Engine applications, check out this [link](https://cloud.google.com/appengine/docs/).

## Below is a preview of the site

### Home Page

![home page](/static/img/home-page.png)

### Sample ascii art listing for animals category Page

![animals ascii art](/static/img/ascii-arts.png)

### Input form for adding ascii art

![submit ascii-art](/static/img/form.png)
