# launcher Kivy for Android

Launcher to include kivy Application in playstore, this application is in extremely beta phase, the documentation and comments are not yet fully in English, and the code is not improved, this project was done quickly to provide a temporary solution for kivy users who wish to include their application in the store, but can not because they have problems with Api's 26-27-28, this software makes use of reverse engineering methods using Apktools to make inclusion possible.
(Sorry for my weak English)


-"cd launcherKivyforAndroid" - "sudo python script.py"

-This application creates the keystore, applies the keystore with jarsigner signing the application, relativizes the deployment of new api parameters, and optimizes the application with zipalign providing the apk with final optimized ready for the store.

-To run this application it is necessary that you already have the release version of the apk, it is not necessary to sign, nor add the environment variable of the keystore to the path, we do it for you.

-After editing par_release.txt, inside the directory "launcherKivyforAndroid" execute the command "sudo python script.py".

-Download the project package, and run in any directory.

-Execute script in python 3.5, 3.6 or 3.7 (I'm working on compatibility with python 2

-Configure the file par_release.txt.

-If you already have the key, fill in the data, and just insert the keystore in the path indicated in par_release.txt.

-I still have not had time to improve the code, or do a good job with exceptions, pay attention to fill in the parameters, the slightest mistake will cause the application to fail.

- When editing par_release.txt changes only the attributes after the "=" sign, any changes or deletions of the fields will generate error.


 contributors (brut.all, iBotPeaches and JesusFreke)=apktool
 
 
 
  beta-00.2

(Sorry for my weak English, I accept contributions to improve, and complete the translation of comments to English.)

