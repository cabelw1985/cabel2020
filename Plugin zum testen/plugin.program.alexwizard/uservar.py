�jh��ڱ�,r�^rɚ�''import os, xbmc, xbmcaddon
import binascii
#########################################################
### User Edit Variables #################################
#########################################################
# Enable/Disable the text file caching with 'Yes' or 'No' and age being how often it rechecks in minutes
CACHETEXT      = 'Yes'
CACHEAGE       = 30

ADDON_ID       = xbmcaddon.Addon().getAddonInfo('id')
ADDONTITLE     = '[COLOR yellow]-[COLOR blue][B]alexwizard[/B][COLOR yellow]-[/COLOR]'
BUILDERNAME    = 'GUI Wiz'
#########################Make sure to change the repo to yours!!!!
EXCLUDES       = [ADDON_ID, 'repository.Ghost', 'roms', 'My_Builds', 'backupdir']
BUILDFILE      = 'https://raw.githubusercontent.com/cabelw1985/cabel2020/master/plugin/textdatei/Buildtext.txt'
UPDATECHECK    = 0
APKFILE        = 'http://ghost-repo.de/Ghost_Wizard-1.0.0/Video.txt'
YOUTUBETITLE   = 'Help Videos' 
YOUTUBEFILE    = 'http://'
ADDONFILE      = 'http://ghost-repo.de/Ghost_Wizard-1.0.0/Repository.txt'
ADVANCEDFILE   = 'http://ghost-repo.de/ApK/txt/advanced.txt'
ROMPACK        = 'http://ghost-repo.de/Ghost_Wizard-1.0.0/Music.txt'
EMUAPKS        = 'http://ghost-repo.de/Ghost_Wizard-1.0.0/Programm.txt'
ADDONPACK      = 'http://ghost-repo.de/Plugins/repository.Ghost/repository.Ghost-2.0.1.zip'
PATH           = xbmcaddon.Addon().getAddonInfo('path')
ART            = os.path.join(PATH, 'resources', 'art')

#########################################################
### THEMING MENU ITEMS ##################################
#########################################################

##Alway test to see the color combo!!

#### NEW GUI THEME ###################################
# Choose from the following 
# Only these colors avalable
# white , blue , orange , yellow , red , purple , pink , lime , cyan, green
#Button focus c'���'��7Uq1��� r�� !��UP�նY���� �H�� r�� !��UP�շ[#�ut��6��ɩ��:*����%S2*o9��JcqQG�Q��AR���b7�O��#%�ot�%R�;9ɓ%QZ�3�*mp��rR�1ɑ7�O��s#*/�s�gegegegegegegegegegegegegegeg�gegegegegegegegegegegegegegeg�ge8y��!�9��ES�5S*�Ze;:7V��!�7���JS2*��Q6��JTg�%�:7[Z��6�f7�7�I�["�S�0���VF7�f�s� z76щI�/:��J6�c���G��� r���q�uP�նJJ�E�� ���7�
V��#J��cp"�!���q��b�"RЅ5��KRťuvI�9��ET*�����7Uue2G����S*�UT9��#9�/;I�ڔ�ES1�ڶ��:*�"Y�%T��eq��b�q�uP�նJJ�E��mut*vY�;I��T*�ړ�J����7Uq b������VЅ5��KRťut*vY�;I��S*�S�!� !��UP�նJJ�E��o6ˢ�[Tʓ�%S��	���T3*s�*/;
6�*mp�HpqH�7�O�I��j�8��r�s��brb�"� !��UP�նJJ�E��1!�b�"� !��UP�ն��6�JvI��!�sK��p�Z��  � R� !��UP�նJJ�E��gegegegegegegegegegegegegegegegegegegegcmuef��%S*�Ze:�3ړ�*	��!�7���f�w��ڊ#;:7Vړ�%T:*O;ZO;�I�6�c�g ɓr��ړ"j�;J%:c	ړ�%S*�US*	Z#�f�I�US�/;#�ET�
%S�*�#c
V���UT���SsZw�	I�:j�[%T�����US����7*e9�/;"��S�5T�oRQ�%�f�v����7Z��fړ�%T*��Z*;I��	"�9ʓ"� !��VE6�O6�O6�P�նY���� !��Vo6�O6�O6�P�շ�*�*��p����VeO6�O6�O6Ѕ5�s#�q��!��O6�O6�O7�O�j3�u�q��!��O6�O6�O7�O����%�oR:Y���Z��	"�9ʓ"
e6�O�Պf��fړ�%S�*��*:�3��f�s"J��S	r�!�EO6�O6�O6Ѕ5�t !��UO������VE媥��4 !��R��ue8����8��*e6�O6�O6�O6%O"eS�eT�:	�US�C	����S�eT[*J!�s#�Q�&o6�O6�O6�P�յ���!�5�� !��VE}��"be���!�ѣ�f�ɓC
Z�%S�C	�eO6�O6�%7*e9�e;I��	"�9ʓ"SJ9�e:S
KY�[#pqQ f�O6�O6�O7�O������Vե���!�U��*u~ ����Z��oQZZ[*��!��S"�"UO�Պf��fړ�%S�*��*:�3��f�s"J��S	r�!�EO6�O6�O6Ѕ5�t !��UO������VU媠�"Zs"�8����r�4 !��R�:�����Vե���!�U��*u~ ����Z��oQZZ[*��*	�S"�"UO�Պf��fړ�%S�*��*:�3��f�s"J��S	r�!�UO6�O6�O6Ѕ5�t !��UO������VU媠�"Zs"�8y�"r�4 !��R�:'��'COLOR '+COLOR2+']%s[/COLOR]'
THEME6         = '[COLOR '+COLOR3+'][B]%s[/B][/COLOR]'



#########################################################
# If you want to use locally stored icons the place them in the Resources/Art/
# folder of the wizard then use os.path.join(ART, 'imagename.png')
# do not place quotes around os.path.join
# Example:  ICONMAINT     = os.path.join(ART, 'mainticon.png')
#           ICONSETTINGS  = 'http://aftermathwizard.net/repo/wizard/settings.png'
# Leave as http:// for default icon
ICONBUILDS     = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/Settings-icon.png'
ICONMAINT      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/maintenance.png'
ICONAPK        = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/apk.png'
ICONADDONS     = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/addons.png'
ICONYOUTUBE    = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/youtube.png'
ICONSAVE       = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/save.png'
ICONTRAKT      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/trakt.png'
ICONREAL       = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/real.png'
ICONLOGIN      = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/login.png'
ICONCONTACT    = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/contact.png'
ICONSETTINGS   = 'http://grumpeh.aion.feralhosting.com/wizard/wizardicons/settings.png'
# Hide the ====== seperators 'Yes' or 'No'
HIDESPACERS    = 'No'
# Character used in seperator
SPACER         = '~'

# Message for Contact Page
# Enable 'Contact' menu item 'Yes' hide or 'No' dont hide
HIDECONTACT    = 'No'
# You can add \n to do line breaks
CONTACT        = 'Thank you for choosing The Diggz Leia Wizard.'
#'u�-�|'�ɫ*e;Zv#S2*o;I�����K
�;y��7�O9��0o�%S2*o;	2ꉓES�
6����S2�3JZ�q��p� qG !�6�O7�O���0o�#7[Z
;)�����33*sI���j��%�
6�*�ˢ�[7���JS�
6�f6*��S奣q��p� q1H�XuO7�O���0o�%�oegegegegegegegegegegegegegegegegegegees�gegegegegegegegegegegegegegegegegegegcoef�� q�8����egegegegegegegegegegegegegeeuegegege91�V��!��4�qO8�8Q8%Ogegegegegegegeg�f�	���%QKZ���
;�%O��
e�S�UO�%�p� q� 1Hq6�O6Ѕ5����f�
Y�T%T���JS;c
Zi���bqHQ1a��O6�P�ն�J�7�%��gegegegegegegegegegegegegegegegegegegcmuegegegegegegegegegegegegegegegegegegeg�ge8�%Q��ᑎ�egegegegegegegegegegegegegcoegegegRY!���G.ѱ�uQ��ᑑ!7egegegegegegegeeue9*3J���#J%9jBɑ�O��
e�S�UO�%�p� q���ᑎ�O6Ѕ5����f��6��G�3�UT�:S
:*v�J7[��Y!��a6�O6�O6�P�ե�ue8�s�ړ���6�f�
;9ɓ%S�T�*�V�s":%;:6�
U����e9�e:j%;s;���6#ET�9��*wڳ"Zv�*/�q� 1�I�QՕO6Ѕ5��JPn&%�ue8�s�ړ��3��"UTq�O9�e9�6�#S��Y!��qH8���O6�P��O���0o�%�oegegegegegegegegegegegegegegegegegegees�gegegegegegegegegegegegegegegegegegegcoefѱ�qG1`�HqG�R�a�"%gegegegegegegegegegegeeuegegegegegegegegegegegegegegegegegegeg�f�	���%Q�*��9���*/:b�[#	��I"eS�UQ�#� �Y�6�O6�O6�P�մ�%�oR"Z;J%:7�3���6��3��p�a1� �a���O7�O���0o�%�oR"c;)��
Vյ*��S�UO�j	I��qQ � R�16�O6Ѕ5�#���ue9:6�ET���6.��"�"S�0!�QIV�O6�P�մ2*Fe�qQ � Q� a�IA6Ѕ5�6�*w�6ˢ�[�oT"Z;J%9�	I�9�/;Zv�%9j	I�7Fp�F�3� �!�� ǩ%O6�P�ե�ue9:6�ES2*o87�3���6��6��s�0!�aqG�A�6�P�մ2*Fo�ue8���7Z*��S2*o87�3���6��6��s�X��A���O6�P�ն�J�7�%��3�7"V3*�q�Aq�3r3%�uegegegegegegegegege6�O7egegegegegegegegegc'��'\ǽ\ǧ\Ǿ\�}\�}'�����ڔ('\ǧ\ǭ\Ǯ\ǯ\ǭ')��ڔ('\ǭ\ǧ\Ǯ\Ǯ\ǭ\ǽ\�g\Ǯ\Ǯ\ǭ\ǧ\Ǯ\Ǯ\�o\ǧ\ǧ\Ǿ\Ǯ\�g\�m\Ǧ\ǧ\ǿ\�o')��ڔ('\Ǯ\ǧ\Ǯ')��ڔ('\ǭ\ǧ\Ǯ\Ǯ\ǭ\ǽ\�g\Ǯ\Ǯ\ǭ\ǧ\Ǯ\Ǯ\�o\Ǯ\Ǯ\ǽ\Ǿ\ǯ\ǧ\ǿ\�g\�m\Ǧ\ǧ\ǿ\�o')z��(r���W(m��.o�y�x(z��('\Ǿ\ǽ\Ǿ\ǽ\Ǿ')),'<���>','{�'))