# Update the .py files for the .ui files.
# Set an environment Variable with a python env that has pyside2
import glob
import os
import subprocess
import shlex

# envfolder = os.getenv('ANACONDA') + "/envs/uai"
envfolder = os.getenv('PYTHON36')
envpython = envfolder + "/python.exe"
envpyside2rcc = envfolder + "/Scripts/pyside2-rcc.exe"
envpyside2uic = envfolder + "/Scripts/pyside2-uic.exe"
envexists = os.path.exists(envfolder)
envpythonexists = os.path.exists(envpython)
envpyside2rccexists = os.path.exists(envpyside2rcc)
loadlocation = os.path.dirname(__file__)
outputLocation = "ui/converted"


def ProcessQRCFiles():
    # CheckOutputFolder()
    # for file in GetUIFiles():
    #     arg = "\""+envpython+"\" " +"\""+envpyside2uic+"\" " + file + " -o " +os.path.join(outputlocation, os.path.splitext(os.path.basename(file))[0]+".py")
    #     arglist = [envpyside2uic, file , "-o",os.path.join(outputlocation, os.path.splitext(os.path.basename(file))[0]+".py")]
    #     print("----------------------------------------------")
    #     print("----------------------------------------------")

    #     print("Running Arg: ", arglist)
    #     print("1()()()()()()()()()()()()()()()()()()()()()()()1")
    #     argproc = subprocess.Popen(arglist, stdout=subprocess.PIPE)
    #     stdout = argproc.communicate()[0]
    #     print ('STDOUT:{}'.format(stdout))
    #     # os.system(arg)
    #     print("Success!: ", arg)
    #     print("----------------------------------------------")
    #     print("----------------------------------------------")

    print("----------------------------------------------")
    print("----------------------------------------------")
    # argg = "\""+envpython+"\" \""+envpyside2uic+"\" resources.qrc -o resources_rc.py"
    argglist = ["pyside2-rcc", "resources.qrc", "-o", "resources_rc.py"]

    print("Running Arg: ", "pyside2-rcc resources.qrc -o resources_rc.py")
    print("3()()()()()()()()()()()()()()()()()()()()()()()2")
    # subprocess.Popen(argglist)

    os.system("pyside2-rcc resources.qrc -o resources_rc.py")
    outputlocation = os.path.dirname(__file__)
    if os.path.exists(os.path.abspath(outputlocation)):
        print("Success!: ", argglist)

        print("Files Exported to: ", os.path.abspath(outputlocation))
        print("Change the 'outputlocation' variable in this Python script to change the output location.")
    else:
        print("Failed : ", argglist)


def WriteTemplateFile(classFilepath):
    file_ = open(os.path.join(os.path.dirname(__file__), "templates/QTWidgetTemplate.py"), 'r')
    data = file_.read()
    file_.close()
    relative_path = os.path.relpath(classFilepath, os.path.dirname(__file__))
    dotpath = os.path.splitext(relative_path.replace("/",".").replace("\\","."))[0]
    dotpathclean = dotpath.replace("..",".")
    convertedPath = os.path.splitext(classFilepath)[0] + '_widgetTemplate.py'
    dataClean = data.replace("%FCLASSNAME%",os.path.splitext(os.path.basename(classFilepath))[0] ).replace("%FPATHDOT%",dotpathclean )
    file_ = open(convertedPath, 'w')
    file_.write(dataClean)
    file_.close()

def CheckOutputFolder():
    if not os.path.exists(outputLocation):
        os.makedirs(outputLocation)


def GetUIFiles():
    return glob.glob(loadlocation + "/*/*.ui")


def ProcessUIFiles():
    global outputLocation
    for file in GetUIFiles():
        outputLocation = os.path.dirname(file)
        arg = "\"" + envpython + "\" " + "\"" + envpyside2uic + "\" " + file + " -o " + os.path.join(outputLocation,
                                                                                                     os.path.splitext(
                                                                                                         os.path.basename(
                                                                                                             file))[
                                                                                                         0] + ".py")
        arglist = [envpyside2uic, file, "-o",
                   os.path.join(outputLocation, os.path.splitext(os.path.basename(file))[0] + ".py")]
        print("----------------------------------------------")
        print("----------------------------------------------")

        print("Running Arg: ", arglist)
        print("1()()()()()()()()()()()()()()()()()()()()()()()1")
        argproc = subprocess.Popen(arglist, stdout=subprocess.PIPE)
        stdout = argproc.communicate()[0]
        print('STDOUT:{}'.format(stdout))
        WriteTemplateFile(os.path.join(outputLocation, os.path.splitext(os.path.basename(file))[0] + ".py"))
        # os.system(arg)
        print("Success!: ", arg)
        print("----------------------------------------------")
        print("----------------------------------------------")

    if os.path.exists(os.path.abspath(outputLocation)):
        print("Success!: ")

        print("Files Exported to: ", os.path.abspath(outputLocation))
        print("Change the 'outputLocation' variable in this Python script to change the output location.")
    else:
        print("Failed : ")


def main():
    if envexists and envpyside2rccexists and envpythonexists:
        ProcessUIFiles()
        ProcessQRCFiles()
    else:
        print("Something doesn't exist! Check your environment variables")
        print("env exists : ", envexists)
        print("env python exists : ", envpythonexists)
        print("env pyside2rcc exists : ", envpyside2rccexists)


if __name__ == '__main__':
    main()
