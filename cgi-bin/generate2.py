#!/usr/bin/python3.6
# Zachary Huang
# zhuang333@wisc.edu
import cgi, os
import cgitb; cgitb.enable()
import traceback
import pandas as pd
from io import StringIO
import datetime


form = cgi.FieldStorage()
# Get filename here.

# Test if the file was uploaded
A = None
try:
    if 'filename2' in form.keys():
        io1 = StringIO(form['filename2'].value.replace("\\n", "\n"))
    else:
        file1 = form['filename1']
        io1 = StringIO(file1.file.read().decode("utf-8"))
    A = pd.read_csv(io1)
    cdate = str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + ".csv"
    A.to_csv("./data/" + cdate)

    column = form['column'].value
    # message  = main.main2(fileitem1, column)
    import subprocess
    cmd = [r"./FAHES", "./data/" + cdate, "./data/", "4", column]
    # p = subprocess.Popen(["./FAHES " + "\"./data/" + cdate + "\" ./data/ 4 \"" + column + "\""], stdout=subprocess.PIPE)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)

    message = p.stdout.read().decode("utf-8")
    try:
        os.remove("./data/" + cdate)
    except OSError:
        pass

except Exception as e:

   message = "<p><font size=\"6\"><b>An error has occured!</b></font></p>"
   message = message + "<p>Please check your csv files according to the error message!</p>"
   message = message + "<p>Key Word for the error is: " + str(e) + "</p>"
   message = message + "<p>Detailed traceback: </p><p>" + traceback.format_exc() + "</p>"




print ("""\
Content-Type: text/html\n
<html>
<body>
<button type="button" onclick="proceed();">Download CSV File</button>

<h2>Result of DMV</h2>
<p id="demo"></p>

<script>
var csvfile = `
""")
# print(form)
# print(fileitem1)
# print(date)
print(message)
print("""`;
document.getElementById("demo").innerHTML = csvfile;
function proceed () {
    var form = document.createElement('form');
    var element1 = document.createElement("input");
    form.setAttribute('method', 'post');
    form.setAttribute('action', "/cgi-bin/download.csv");

    element1.value=csvfile;
    element1.name="csvfile";

    form.appendChild(element1);
    form.style.display = "none";
    document.body.appendChild(form);

    form.submit();
}
</script>

</body>
</html>""")
