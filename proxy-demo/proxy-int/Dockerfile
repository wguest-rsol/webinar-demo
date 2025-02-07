FROM php:8.4.4RC2-apache

# Enable Apache mod_rewrite and additional necessary modules
RUN a2enmod rewrite proxy proxy_http

# Set working directory
WORKDIR /var/www/html

# Copy source files for port 80 from local 'src1' directory
COPY index.php /var/www/html/index.php

# Set correct permissions
RUN chown -R www-data:www-data /var/www/html && \
    chmod -R 755 /var/www/html


# Expose ports 80 and 8000
EXPOSE 80 


# Create a virtual host for port 80 (standard DocumentRoot)
RUN echo '<VirtualHost *:80>' > /etc/apache2/sites-available/000-default.conf && \
    echo '    DocumentRoot /var/www/html' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    <Directory /var/www/html>' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        Options Indexes FollowSymLinks' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        AllowOverride All' >> /etc/apache2/sites-available/000-default.conf && \
    echo '        Require all granted' >> /etc/apache2/sites-available/000-default.conf && \
    echo '    </Directory>' >> /etc/apache2/sites-available/000-default.conf && \
    echo '</VirtualHost>' >> /etc/apache2/sites-available/000-default.conf

# Start Apache 
CMD ["apache2-foreground"]