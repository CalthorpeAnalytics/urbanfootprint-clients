# UrbanFootprint Client Configuration

This repository is included as a [git
submodule](https://github.com/CalthorpeAnalytics/urbanfootprint/blob/master/.gitmodules) in the main
[UrbanFootprint project repository](https://github.com/calthorpeanalytics/urbanfootprint). For
instructions on how to properly configure an UrbanFootprint instance please refer to
[UrbanFootprint's top-level README](https://github.com/CalthorpeAnalytics/urbanfootprint/blob/master/README.md).

## Creating Your Own Client Configurations

The recommended pattern for creating a client configuration for your own organization is to [fork
this repository](https://help.github.com/articles/fork-a-repo/). You can then substitute the URL for
your repository in the setup instructions. For example, in place of cloning the sample 
`urbanfootprint-configuration` repository like this:

    git clone https://github.com/CalthorpeAnalytics/urbanfootprint.git urbanfootprint git clone
    https://github.com/CalthorpeAnalytics/urbanfootprint-configuration.git urbanfootprint-configuration

you would clone *your* forked `urbanfootprint-configuration` repository like this:

    git clone https://github.com/CalthorpeAnalytics/urbanfootprint.git urbanfootprint git clone
    https://github.com/YOUR-ORGANIZATION/urbanfootprint-configuration.git urbanfootprint-configuration

Copyright (C) 2016 Calthorpe Analytics
