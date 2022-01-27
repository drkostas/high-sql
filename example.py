# pip install high-sql
import os
from high_sql import HighMySQL, HighConfig, ColorLogger

table_schema = """
id        int auto_increment primary key,
firstname varchar(30)                         not null,
lastname  varchar(30)                         not null,
email     varchar(50)                         null,
reg_date  timestamp default CURRENT_TIMESTAMP null on update CURRENT_TIMESTAMP
"""
# Setup Logger
log = ColorLogger(logger_name='Example', color='yellow')

# Load config
# db_conf = {'type': 'mysql',
#            'config': {'hostname': 'your hostname', 'username': 'your username',
#                       'password': 'your password', 'db_name': 'your db name', 'port': 3306}}
# config_path = os.path.join('confs', 'conf.yml')
config_path = os.path.join('confs', 'conf_with_env_vars.yml')
config = HighConfig(config_src=config_path)
db_conf = config.get_db_config()
# Check for errors
if db_conf['type'] != 'mysql':
    raise Exception(f"{db_conf['type']} not yet supported!")
if db_conf['config']['username'] == 'MYSQL_USERNAME':
    raise Exception("You are trying to use environmental variables but they are not loaded!")
# Initialize handler
mysql_obj = HighMySQL(config=db_conf['config'])

# -------- Examples -------- #
# Create Table
mysql_obj.create_table(table='test_table', schema=table_schema)
# Show Tables
log.info(f"List of tables in DB:\n{mysql_obj.show_tables()}")
# Insert into table
mysql_obj.insert_into_table('test_table', data={'firstname': 'Mr Name', 'lastname': 'surname'})
# Show the record
res = mysql_obj.select_from_table('test_table', columns='*', where='firstname="Mr Name"',
                                  order_by='firstname', asc_or_desc='ASC', limit=5)
log.info(f"Result:\n{res}")
# Update it
mysql_obj.update_table('test_table', set_data={'lastname': 'New Last Name'},
                       where='firstname="Mr Name"')
# Show the updated record
res = mysql_obj.select_from_table('test_table', columns='*', where='firstname="Mr Name"')
log.info(f"Result:\n{res}")
# Delete it
mysql_obj.delete_from_table('test_table', where='firstname="Mr Name"')
# Show that it is gone
res = mysql_obj.select_from_table('test_table', columns='*', where='firstname="Mr Name"')
log.info(f"Result:\n{res}")
# Truncate Table
mysql_obj.truncate_table('test_table')
# Drop Table
mysql_obj.drop_table('test_table')
