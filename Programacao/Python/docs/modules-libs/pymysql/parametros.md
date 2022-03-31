### Parameters of :  pymysql.connect() :

- host – Host where the database server is located.

- user – Username to log in as.

- password – Password to use.

- database – Database to use, None to not use a particular one.

- port – MySQL port to use, default is usually OK. (default: 3306)

- bind_address – When the client has multiple network interfaces, specify the interface from which to connect to the host. Argument can be a hostname or an IP address.

- unix_socket – Use a unix socket rather than TCP/IP.

- read_timeout – The timeout for reading from the connection in seconds (default: None - no timeout)

- write_timeout – The timeout for writing to the connection in seconds (default: None - no timeout)

- charset – Charset to use.

- sql_mode – Default SQL_MODE to use.

- read_default_file – Specifies my.cnf file to read these parameters from under the [client] section.

- conv – Conversion dictionary to use instead of the default one. This is used to provide custom marshalling and unmarshalling of types. See converters.

- use_unicode – Whether or not to default to unicode strings. This option defaults to true.

- client_flag – Custom flags to send to MySQL. Find potential values in constants.CLIENT.

- cursorclass – Custom cursor class to use.

- init_command – Initial SQL statement to run when connection is established.

- connect_timeout – The timeout for connecting to the database in seconds. (default: 10, min: 1, max: 31536000)

- ssl – A dict of arguments similar to mysql_ssl_set()’s parameters.

- ssl_ca – Path to the file that contains a PEM-formatted CA certificate.

- ssl_cert – Path to the file that contains a PEM-formatted client certificate.

- ssl_disabled – A boolean value that disables usage of TLS.

- ssl_key – Path to the file that contains a PEM-formatted private key for the client certificate.

- ssl_verify_cert – Set to true to check the server certificate’s validity.

- ssl_verify_identity – Set to true to check the server’s identity.

- read_default_group – Group to read from in the configuration file.

- autocommit – Autocommit mode. None means use server default. (default: False)

- local_infile – Boolean to enable the use of LOAD DATA LOCAL command. (default: False)

- max_allowed_packet – Max size of packet sent to server in bytes. (default: 16MB) Only used to limit size of “LOAD LOCAL INFILE” data packet smaller than default (16KB).

- defer_connect – Don’t explicitly connect on construction - wait for connect call. (default: False)

- auth_plugin_map – A dict of plugin names to a class that processes that plugin. The class will take the Connection object as the argument to the constructor. The class needs an authenticate method taking an authentication packet as an argument. For the dialog plugin, a prompt(echo, prompt) method can be used (if no authenticate method) for returning a string from the user. (experimental)

- server_public_key – SHA256 authentication plugin public key value. (default: None)

- binary_prefix – Add '_ binary' prefix on bytes and bytearray. (default: False)

- compress – Not supported.

- named_pipe – Not supported.

- db – DEPRECATED Alias for database.

- passwd – DEPRECATED Alias for password.