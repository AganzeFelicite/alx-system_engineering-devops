#to set up a new server with all the configuration we have 
#done sofar using bash


exec {'install Nginx':
  provider => shell,
  command  => 'sudo apt-get -y update,
  command  => sudo apt-get -y install nginx,
  command  => echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html,
  command  => sudo sed -i "s/server_name _;/server_name _;\n\tadd_header X-Served-By $(hostname);
 	 \n\trewrite ^\/redirect_me https:\/\/github.com\/Theocode12 permanent;/"/etc/nginx/sites-available/default;
  command  => sudo service nginx start',

}
