#/bin/bash

echo "Import file $1 file "


#/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -q "CREATE DB myDB"

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -i "/scripts/$1.sql"
