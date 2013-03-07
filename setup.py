from subprocess import call

print "\nCreating Virtual Environment\n"
print "============================\n"
call(['python', 'virtualenv.py', 'box'])
print "\nVirtual Environment Created\n"

print "\nInstalling Django\n"
print "=================\n"
call(['box/bin/pip', 'install', 'django'])
print "\nDjango Installed\n"

print "\nInstalling PostgreSQL Driver\n"
print "============================\n"
call(['box/bin/pip', 'install', 'psycopg2'])
print "\nPostgreSQLDriver Installed\n"

print "\nInstalling MySQL Driver\n"
print "=======================\n"
call(['box/bin/pip', 'install', 'mysql-python'])
print "\nMySQLDriver Installed\n"

print "\nCreating Initial Django Project\n"
print "===============================\n"
call(['box/bin/django-admin.py', 'startproject', 'newproject'])

print "\n\nYour new Django Environment is ready!\n\n"
