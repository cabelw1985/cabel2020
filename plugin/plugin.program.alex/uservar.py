import os, xbmc, xbmcaddon

#########################################################
### User Edit Variables #################################
#########################################################
ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = 'alex wizard'
EXCLUDES       = [ADDON_ID]
# Text File with build info in it.
BUILDFILE      = 'https://raw.githubusercontent.com/cabelw1985/cabelplugin/master/alexplugintext/autobuilds.txt'
# How often you would list it to check for build updates in days
# 0 being every startup of kodi
UPDATECHECK    = 0
# Text File with apk info in it.
APKFILE        = 'https://raw.githubusercontent.com/cabelw1985/cabelplugin/master/text/apk.txt'
# Text File with Youtube Videos urls.  Leave as 'http://' to ignore
YOUTUBETITLE   = 'YouTube Storm Tutorials'
YOUTUBEFILE    = 'https://raw.githubusercontent.com/cabelw1985/cabelplugin/master/text/youtube.txt'
# Text File for addon installer.  Leave as 'http://' to ignore
ADDONFILE      = 'http://sgkodi.de/Wizard-Daten/Addons/addons.txt'
# Text File for advanced settings.  Leave as 'http://' to ignore
ADVANCEDFILE   = 'http://sgkodi.de/Wizard-Daten/AS/advancedsettings.txt'

# Dont need to edit just here for icons stored locally
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONMAINT      = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png' 
ICONAPK        = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONADDONS     = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONADVANCED   = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONBACKUP     = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONSPEED      = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONYOUTUBE    = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONSAVE       = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONTRAKT      = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONREAL       = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONCONTACT    = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONSETTINGS   = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONCLEAN      = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONLOG        = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
ICONPAY        = 'https://raw.github.com/cabelw1985/cabelplugin/master/Bilder/wizard/builds.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '='

# You can edit these however you want, just make sure that you have a %s in each of the
# THEME's so it grabs the text from the menu item
COLOR1         = 'blue'
COLOR2         = 'white'
# Primary menu items   / %s is the menu item and is required
THEME1         = '[COLOR '+COLOR1+'][B][I][COLOR '+COLOR2+'][/COLOR][/B][/COLOR] [COLOR '+COLOR2+']%s[/COLOR][/I]'
# Build Names          / %s is the menu item and is required
THEME2         = '[COLOR '+COLOR2+']%s[/COLOR]'
# Alternate items      / %s is the menu item and is required
THEME3         = '[COLOR '+COLOR1+']%s[/COLOR]'
# Current Build Header / %s is the menu item and is required
THEME4         = '[COLOR '+COLOR1+']Aktuelles Build:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'
# Current Theme Header / %s is the menu item and is required
THEME5         = '[COLOR '+COLOR1+']Aktuelles Theme:[/COLOR] [COLOR '+COLOR2+']%s[/COLOR]'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Cabel Wizard'
#Images used for the contact window.  http:// for default icon and fanart
CONTACTICON    = ''
CONTACTFANART  = ''
#########################################################

#########################################################
### AUTO UPDATE #########################################
########## FOR THOSE WITH NO REPO #######################
# Enable Auto Update 'Yes' or 'No'
AUTOUPDATE     = 'Yes'
# Url to wizard version
WIZARDFILE     = 'https://raw.github.com/cabelw1985/cabelplugin//master/text/autobuilds.txt'
#########################################################

#########################################################
### AUTO INSTALL ########################################
########## REPO IF NOT INSTALLED ########################
# Enable Auto Install 'Yes' or 'No'
AUTOINSTALL    = 'Yes'
# Addon ID for the repository
REPOID         = 'repository.cabel'
# Url to Addons.xml file in your repo folder(this is so we can get the latest version)
REPOADDONXML   = 'https://raw.githubusercontent.com/cabelw1985/repocabel/master/zip/repository.cabel/addon.xml'
# Url to folder zip is located in
REPOZIPURL     = 'https://raw.github.com/cabelw1985/repocabel/master/zip/repository.cabel/'
#########################################################

#########################################################
### NOTIFICATION WINDOW##################################
#########################################################
# Enable Notification screen Yes or No
ENABLE         = 'YES'
# Url to notification file
NOTIFICATION   = 'https://raw.github.com/cabelw1985/cabelplugin/master/text/notify.txt'
# Use either 'Text' or 'Image'
HEADERTYPE     = 'Text'
HEADERMESSAGE  = 'Cabel Wizard'
# url to image if using Image 424x180
HEADERIMAGE    = ''
# Background for Notification Window
BACKGROUND     = ''
###################################################################
#																  #
# Translated and modified by SGK / Kodi Unlimited Support 03.2018 #
#																  #
###################################################################