FROM php:8.4.4RC2-apache

# Enable Apache mod_rewrite and additional necessary modules
RUN a2enmod rewrite proxy proxy_http

# Set working directory
WORKDIR /var/www/html

# Copy source files for port 80 from local 'src1' directory
COPY src1/ /var/www/html/

# Set correct permissions
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html

# Create a new directory for the HTML document root for port 8000
RUN mkdir /var/www/html8000

# Copy source files for port 8000 from local 'src2' directory into the new root
COPY src2/ /var/www/html8000/

# Set correct permissions for the new document root
RUN chown -R www-data:www-data /var/www/html8000 && \
    chmod -R 755 /var/www/html8000

# Expose ports 80 and 8000
EXPOSE 80 8000

# Configure Apache to listen on both port 80 and 8000
RUN echo "Listen 127.0.0.1:8000" >> /etc/apache2/ports.conf

# Create a virtual host for port 80 (standard DocumentRoot)
RUN echo '<VirtualHost *:80>' > /etc/apache2/sites-available/000-default.conf && \
    echo '    DocumentRoot /var/www/html' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    <Directory /var/www/html>' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        Options Indexes FollowSymLinks' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        AllowOverride All' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        Require all granted' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    </Directory>' >> /etc/apache2/sites-available/000-default.conf && \
    echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf

# Create a virtual host for port 8000 (different DocumentRoot)
RUN echo '<VirtualHost 127.0.0.1:8000>' > /etc/apache2/sites-available/000-default-8000.conf && \
    echo '    DocumentRoot /var/www/html8000' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '    <Directory /var/www/html8000>' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '        Options Indexes FollowSymLinks' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '        AllowOverride All' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '        Require all granted' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '    </Directory>' >> /etc/apache2/sites-available/000-default-8000.conf && \
    echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default-8000.conf

# Enable the site configuration for port 8000
RUN a2ensite 000-default-8000.conf

# Start Apache 
CMD ["apache2-foreground"]