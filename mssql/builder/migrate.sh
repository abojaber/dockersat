#/bin/bash

echo "Run /data/scripts.sql file only when build the image..."


#/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -q "CREATE DB myDB"

/opt/mssql-tools/bin/sqlcmd -S localhost -U sa -P $SA_PASSWORD -q "CREATE DB myDB"

