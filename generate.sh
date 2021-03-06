
#!/bin/bash
echo -e "\nGenerating a options.config file"

  # Generate the file
  cat > ./src/.ebextensions/options.config <<EOL
option_settings:
  aws:elasticbeanstalk:application:environment:
    SENDGRID_API_KEY: ${SENDGRID_API_KEY}
    DJANGO_ALLOWED_HOSTS: ${DJANGO_ALLOWED_HOSTS}
    DJANGO_SETTINGS_MODULE: ${DJANGO_SETTINGS_MODULE}
    GOOGLE_ANALYTICS_KEY: ${GOOGLE_ANALYTICS_KEY}
    FE_E2E_TEST_USER_EMAIL: ${FE_E2E_TEST_USER_EMAIL}
    GOOGLE_ANALYTICS_CLIENT_ID: ${GOOGLE_ANALYTICS_CLIENT_ID}
    DJANGO_SECRET_KEY: ${DJANGO_SECRET_KEY}
    E2E_TEST_AUTH_TOKEN: ${E2E_TEST_AUTH_TOKEN}
    DATABASE_URL: ${DATABASE_URL}
