# <p align="center">Antipetros Discordbot</p>


<p align="center"><img src="art/finished/images/AntiPetros_for_readme.png" alt="Antipetros Discordbot Avatar"/></p>


---

## ToC



  
  - [Installation](#installation)    
    - [PyPi](#pypi)  
  - [Usage](#usage)  
  - [Description](#description)  
  - [Features](#features)  
  - [Dependencies](#dependencies)    
    - [Python dependencies](#python-dependencies)    
    - [External dependencies](#external-dependencies)  
  - [License](#license)  
  - [Development](#development)    
    - [Future Plans](#future-plans)  
  - [See also](#see-also)    
    - [Links](#links)



---



__**Bot-Name:**__

> AntiPetros

__**Version:**__

> 1.1.7





---

## Installation



### PyPi

```shell
pip install antipetros_discordbot==1.1.7
```



---

## Usage




- __**antipetrosbot clean**__
    > Cli command to clean the 'APPDATA' folder that was created.


- __**antipetrosbot run**__
    > Standard way to start the bot and connect it to discord.


- __**antipetrosbot stop**__
    > Cli way of autostoping the bot.





---

## Description







---

## Features




<details><summary><b>Currently usable Cogs</b></summary><blockquote>



### <p align="center"><b>[AdministrationCog](antipetros_discordbot/cogs/discord_admin_cogs/discord_admin_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Commands and methods that help in Administrate the Discord Server.</blockquote>

#### Config Name

<blockquote>administration</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- OUTDATED

- NEEDS_REFRACTORING

- FEATURE_MISSING

- UNTESTED

- OPEN_TODOS
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **DELETE_MSG**
    

    
    - **aliases:** *delete-msg*, *deletemsg*, *delete.msg*, *delete+msg*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[AntistasiLogWatcherCog](antipetros_discordbot/cogs/antistasi_tool_cogs/antistasi_log_watcher_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>soon</blockquote>

#### Config Name

<blockquote>antistasi_log_watcher</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING

- UNTESTED

+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **GET_NEWEST_LOGS**
    
    - **help:**

        Gets the newest log files from the Dev Drive.
        
        If the log file is bigger than current file size limit, it will provide it zipped.
        
        Tries to fuzzy match both server and sub-folder.
        
        Args:
            server (str): Name of the Server
            sub_folder (str): Name of the sub-folder e.g. Server, HC_0, HC_1,...
            amount (int, optional): The amount of log files to get. standard max is 5 . Defaults to 1.

    

    
    - **aliases:** *get-newest-logs*, *getnewestlogs*, *get.newest.logs*, *get+newest+logs*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros get_newest_logs mainserver_1 server
        ```
    
    <br>


- **GET_NEWEST_MOD_DATA**
    
    - **help:**

        Gets the required mods for the Server.
        
        Provides the list as embed and Arma3 importable html file.
        
        Args:
            server (str): Name of the Antistasi Community Server to retrieve the mod list.

    

    
    - **aliases:** *getnewestmoddata*, *get-newest-mod-data*, *get+newest+mod+data*, *get.newest.mod.data*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros get_newest_mod_data mainserver_1
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[BotAdminCog](antipetros_discordbot/cogs/bot_admin_cogs/bot_admin_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Commands and methods that are needed to Administrate the Bot itself.</blockquote>

#### Config Name

<blockquote>bot_admin</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **ADD_TO_BLACKLIST**
    

    
    - **aliases:** *add-to-blacklist*, *add+to+blacklist*, *add.to.blacklist*, *addtoblacklist*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **ADD_WHO_IS_PHRASE**
    

    
    - **aliases:** *add.who.is.phrase*, *addwhoisphrase*, *add-who-is-phrase*, *add+who+is+phrase*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **ALL_ALIASES**
    

    
    - **aliases:** *all-aliases*, *allaliases*, *all+aliases*, *all.aliases*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **INVOCATION_PREFIXES**
    

    
    - **aliases:** *invocation+prefixes*, *invocation.prefixes*, *invocation-prefixes*, *invocationprefixes*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **LIFE_CHECK**
    

    
    - **aliases:** *are-you-there*, *poke-with-stick*, *life+check*, *life-check*, *life.check*, *you_dead?*, *lifecheck*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **REMOVE_FROM_BLACKLIST**
    

    
    - **aliases:** *removefromblacklist*, *remove+from+blacklist*, *remove.from.blacklist*, *remove-from-blacklist*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **SELF_ANNOUNCEMENT**
    

    
    - **aliases:** *self-announcement*, *self+announcement*, *selfannouncement*, *self.announcement*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **SEND_LOG_FILE**
    
    - **help:**

        Gets the log files of the bot and post it as a file to discord.
        
        You can choose to only get the newest or all logs.
        
        Args:
            which_logs (str, optional): [description]. Defaults to 'newest'. other options = 'all'

    

    
    - **aliases:** *send+log+file*, *send-log-file*, *sendlogfile*, *send.log.file*
    

    - **is hidden:** True

    - **usage:**
        ```python
        @AntiPetros send_log_file all
        ```
    
    <br>


- **TELL_UPTIME**
    

    
    - **aliases:** *tell+uptime*, *tell.uptime*, *telluptime*, *tell-uptime*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **TELL_VERSION**
    

    
    - **aliases:** *tell-version*, *tellversion*, *tell.version*, *tell+version*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[CommunityServerInfoCog](antipetros_discordbot/cogs/antistasi_tool_cogs/community_server_info_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>soon</blockquote>

#### Config Name

<blockquote>community_server_info</blockquote>


#### Cog State Tags

```diff
- EMPTY

- DOCUMENTATION_MISSING

- CRASHING

- OUTDATED

- FEATURE_MISSING

- UNTESTED
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **CURRENT_ONLINE_SERVER**
    
    - **help:**

        Shows all server of the Antistasi Community, that are currently online.
        
        Testserver_3 and Eventserver are excluded as they usually are password guarded.

    

    
    - **aliases:** *current-online-server*, *current+online+server*, *currentonlineserver*, *current.online.server*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros current_online_server
        ```
    
    <br>


- **CURRENT_PLAYERS**
    
    - **help:**

        Show all players that are currently online on one of the Antistasi Community Server.
        
        Shows Player Name, Player Score and Time Played on that Server.
        
        Args:
            server (str): Name of the Server, case insensitive.

    

    
    - **aliases:** *current-players*, *currentplayers*, *current.players*, *current+players*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros current_players mainserver_1
        ```
    
    <br>


- **EXCLUDE_FROM_SERVER_STATUS_NOTIFICATION**
    

    
    - **aliases:** *exclude-from-server-status-notification*, *exclude.from.server.status.notification*, *excludefromserverstatusnotification*, *exclude+from+server+status+notification*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **UNDO_EXCLUDE_FROM_SERVER_STATUS_NOTIFICATION**
    

    
    - **aliases:** *undo.exclude.from.server.status.notification*, *undo+exclude+from+server+status+notification*, *undoexcludefromserverstatusnotification*, *undo-exclude-from-server-status-notification*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[ConfigCog](antipetros_discordbot/cogs/bot_admin_cogs/config_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Cog with commands to access and manipulate config files, also for changing command aliases.
Almost all are only available in DM's

commands are hidden from the help command.</blockquote>

#### Config Name

<blockquote>config</blockquote>


#### Cog State Tags

```diff
- NEEDS_REFRACTORING

- FEATURE_MISSING

- OPEN_TODOS
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **ADD_ALIAS**
    
    - **help:**

        Adds an alias for a command.
        
        Alias has to be unique and not spaces.
        
        Args:
            command_name (str): name of the command
            alias (str): the new alias.

    

    
    - **aliases:** *add.alias*, *addalias*, *add+alias*, *add-alias*
    

    - **is hidden:** True

    - **usage:**
        ```python
        @AntiPetros add_alias flip_coin flip_it
        ```
    
    <br>


- **CHANGE_SETTING_TO**
    
    - **help:**

        NOT IMPLEMENTED

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **CONFIG_REQUEST**
    
    - **help:**

        Returns a Config file as and attachment, with additional info in an embed.
        
        Args:
            config_name (str, optional): Name of the config, or 'all' for all configs. Defaults to 'all'.

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **LIST_CONFIGS**
    
    - **help:**

        NOT IMPLEMENTED

    

    
    - **aliases:** *list.configs*, *list+configs*, *list-configs*, *listconfigs*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **OVERWRITE_CONFIG_FROM_FILE**
    
    - **help:**

        NOT IMPLEMENTED

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **SHOW_CONFIG_CONTENT**
    
    - **help:**

        NOT IMPLEMENTED

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **SHOW_CONFIG_CONTENT_RAW**
    
    - **help:**

        NOT IMPLEMENTED

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[FaqCog](antipetros_discordbot/cogs/special_channels_cogs/faq_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Creates Embed FAQ items.</blockquote>

#### Config Name

<blockquote>faq</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING

- UNTESTED

+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **POST_FAQ_BY_NUMBER**
    
    - **help:**

        Posts an FAQ as an embed on request.
        
        Either as an normal message or as an reply, if the invoking message was also an reply.
        
        Deletes invoking message
        
        Args:
            faq_numbers (commands.Greedy[int]): minimum one faq number to request, maximum as many as you want seperated by one space (i.e. 14 12 3)
            as_template (bool, optional): if the resulting faq item should be created via the templated items or from the direct parsed faqs.

    

    
    - **aliases:** *faq*, *post-faq-by-number*, *postfaqbynumber*, *post.faq.by.number*, *post+faq+by+number*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---





### <p align="center"><b>[GiveAwayCog](antipetros_discordbot/cogs/community_events_cogs/give_away_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Soon</blockquote>

#### Config Name

<blockquote>give_away</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **ABORT_GIVE_AWAY**
    
    - **help:**

        NOT IMPLEMENTED

    

    
    - **aliases:** *abort+give+away*, *abort-give-away*, *abort.give.away*, *abortgiveaway*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **CREATE_GIVEAWAY**
    

    
    - **aliases:** *creategiveaway*, *giveaway*, *create-giveaway*, *create+giveaway*, *create.giveaway*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **FINISH_GIVE_AWAY**
    
    - **help:**

        NOT IMPLEMENTED

    

    
    - **aliases:** *finish.give.away*, *finishgiveaway*, *finish-give-away*, *finish+give+away*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[ImageManipulatorCog](antipetros_discordbot/cogs/general_cogs/image_manipulation_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Commands that manipulate or generate images.</blockquote>

#### Config Name

<blockquote>image_manipulation</blockquote>


#### Cog State Tags

```diff
- NEEDS_REFRACTORING

- FEATURE_MISSING

- OPEN_TODOS

+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **ADD_STAMP**
    
    - **help:**

        Adds a new stamp image to the available stamps.
        
        This command needs to have the image as an attachment.

    

    
    - **aliases:** *addstamp*, *add+stamp*, *add.stamp*, *add-stamp*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros add_stamp
        ```
    
    <br>


- **AVAILABLE_STAMPS**
    
    - **help:**

        Posts all available stamps.

    

    
    - **aliases:** *available-stamps*, *available.stamps*, *available+stamps*, *availablestamps*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros available_stamps
        ```
    
    ![](art/finished/gifs/available_stamps_command.gif)
    
    <br>


- **MEMBER_AVATAR**
    
    - **help:**

        Stamps the avatar of a Member with the Antistasi Crest.
        
        Returns the new stamped avatar as a .PNG image that the Member can save and replace his orginal avatar with.
        
        Example:
            @AntiPetros member_avatar

    

    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **STAMP_IMAGE**
    
    - **help:**

        Stamps an image with a small image from the available stamps.
        
        Usefull for watermarking images.
        
        Get all available stamps with '@AntiPetros available_stamps'

    

    
    - **aliases:** *stamp.image*, *stamp+image*, *stamp-image*, *stampimage*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros stamp_image -si ASLOGO -fp bottom -sp right -so 0.5 -f 0.25
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[KlimBimCog](antipetros_discordbot/cogs/general_cogs/klim_bim_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Collection of small commands that either don't fit anywhere else or are just for fun.</blockquote>

#### Config Name

<blockquote>klim_bim</blockquote>


#### Cog State Tags

```diff
+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **FLIP_COIN**
    
    - **help:**

        Simulates a coin flip and posts the result as an image of a Petros Dollar.

    

    
    - **aliases:** *flip.coin*, *flipcoin*, *flip+coin*, *coinflip*, *flip-coin*, *flip*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros flip_coin
        ```
    
    ![](art/finished/gifs/flip_coin_command.gif)
    
    <br>


- **MAKE_FIGLET**
    
    - **help:**

        Posts an ASCII Art version of the input text.
        
        **Warning, your invoking message gets deleted!**
        
        Args:
            text (str): text you want to see as ASCII Art.

    

    
    - **aliases:** *make+figlet*, *make-figlet*, *makefiglet*, *make.figlet*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros make_figlet The text to figlet
        ```
    
    ![](art/finished/gifs/make_figlet_command.gif)
    
    <br>


- **SHOW_USER_INFO**
    

    
    - **aliases:** *showuserinfo*, *show-user-info*, *show+user+info*, *show.user.info*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **THE_DRAGON**
    
    - **help:**

        Posts and awesome ASCII Art Dragon!

    

    
    - **aliases:** *the.dragon*, *the-dragon*, *thedragon*, *the+dragon*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros the_dragon
        ```
    
    ![](art/finished/gifs/the_dragon_command.gif)
    
    <br>


- **URBAN_DICTIONARY**
    
    - **help:**

        Searches Urbandictionary for the search term and post the answer as embed
        
        Args:
        
            term (str): the search term
            entries (int, optional): How many UD entries for that term it should post, max is 5. Defaults to 1.

    

    
    - **aliases:** *urban-dictionary*, *urban+dictionary*, *urban.dictionary*, *urbandictionary*
    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros urban_dictionary Petros 2
        ```
    
    ![](art/finished/gifs/urban_dictionary_command.gif)
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[PerformanceCog](antipetros_discordbot/cogs/bot_admin_cogs/performance_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Collects Latency data and memory usage every 10min and posts every 24h a report of the last 24h as graphs.</blockquote>

#### Config Name

<blockquote>performance</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- NEEDS_REFRACTORING

- FEATURE_MISSING

- OPEN_TODOS
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **GET_COMMAND_STATS**
    

    
    - **aliases:** *get+command+stats*, *get.command.stats*, *getcommandstats*, *get-command-stats*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **REPORT**
    
    - **help:**

        Reports both current latency and memory usage as Graph.

    

    

    - **is hidden:** True

    - **usage:**
        ```python
        @AntiPetros report
        ```
    
    <br>


- **REPORT_LATENCY**
    

    
    - **aliases:** *reportlatency*, *report.latency*, *report+latency*, *report-latency*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **REPORT_MEMORY**
    

    
    - **aliases:** *report-memory*, *report+memory*, *report.memory*, *reportmemory*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[PurgeMessagesCog](antipetros_discordbot/cogs/discord_admin_cogs/purge_messages_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Soon</blockquote>

#### Config Name

<blockquote>purge_messages</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **PURGE_ANTIPETROS**
    

    
    - **aliases:** *purgeantipetros*, *purge.antipetros*, *purge+antipetros*, *purge-antipetros*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[SaveSuggestionCog](antipetros_discordbot/cogs/general_cogs/save_suggestion_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Provides functionality for each Antistasi Team to save suggestions by reacting with emojis.</blockquote>

#### Config Name

<blockquote>save_suggestion</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- NEEDS_REFRACTORING

- FEATURE_MISSING

- UNTESTED

- OPEN_TODOS

+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **AUTO_ACCEPT_SUGGESTIONS**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **CLEAR_ALL_SUGGESTIONS**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **GET_ALL_SUGGESTIONS**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **MARK_DISCUSSED**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **REMOVE_ALL_USERDATA**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **REQUEST_MY_DATA**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **UNSAVE_SUGGESTION**
    

    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[SubscriptionCog](antipetros_discordbot/cogs/discord_admin_cogs/subscription_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Soon</blockquote>

#### Config Name

<blockquote>subscription</blockquote>


#### Cog State Tags

```diff
- DOCUMENTATION_MISSING

- FEATURE_MISSING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **CREATE_SUBSCRIPTION_CHANNEL**
    

    
    - **aliases:** *create.subscription.channel*, *createsubscriptionchannel*, *create-subscription-channel*, *create+subscription+channel*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **NEW_TOPIC**
    

    
    - **aliases:** *new-topic*, *new+topic*, *new.topic*, *newtopic*
    

    - **is hidden:** True

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[TemplateCheckerCog](antipetros_discordbot/cogs/antistasi_tool_cogs/template_checker_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>soon</blockquote>

#### Config Name

<blockquote>template_checker</blockquote>


#### Cog State Tags

```diff
- EMPTY

- DOCUMENTATION_MISSING

- CRASHING

- OUTDATED

- FEATURE_MISSING

- UNTESTED
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **CHECK_TEMPLATE**
    
    - **help:**

        Checks all Classnames inside a provided template.
        
        Needs to have the tempalte as attachment to the invoking message.
        
        Returns the list of classnames it can't find in the config along with possible correction.
        
        Returns also a corrected version of the template file.
        
        Args:
            all_items_file (bool, optional): if it should also provide a file that lists all used classes. Defaults to True.
            case_insensitive (bool, optional): if it should check Case insentive. Defaults to False.

    

    
    - **aliases:** *check.template*, *checktemplate*, *check-template*, *check+template*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>



</blockquote>

</details>

---



### <p align="center"><b>[TranslateCog](antipetros_discordbot/cogs/general_cogs/translate_cog.py)</b></p>

<details><summary><b>Description</b></summary>




#### Short Description

<blockquote>Collection of commands that help in translating text to different Languages.</blockquote>

#### Config Name

<blockquote>translate</blockquote>


#### Cog State Tags

```diff
+ WORKING
```

</details>

<details><summary><b>Commands</b></summary><blockquote>


- **AVAILABLE_LANGUAGES**
    

    
    - **aliases:** *availablelanguages*, *available-languages*, *available.languages*, *available+languages*
    

    - **is hidden:** False

    - **usage:**
        ```python
        None
        ```
    
    <br>


- **TRANSLATE**
    
    - **help:**

        Translates text into multiple different languages.
        
        Tries to auto-guess input language.
        
        **Warning, your invoking message gets deleted!**
        
        Args:
            text_to_translate (str): the text to translate, quotes are optional
            to_language_id (Optional[LanguageConverter], optional): either can be the name of the language or an language code (iso639-1 language codes). Defaults to "english".

    

    

    - **is hidden:** False

    - **usage:**
        ```python
        @AntiPetros translate german This is the Sentence to translate
        ```
    
    ![](art/finished/gifs/translate_command.gif)
    
    <br>



</blockquote>

</details>

---


</blockquote></details>



---

## Dependencies



**Developed with Python Version `3.9.1`**

### Python dependencies


- **Jinja2** *2.11.2*

- **Pillow** *8.1.2*

- **WeasyPrint** *52.2*

- **aiohttp** *3.7.3*

- **aiosqlite** *0.16.1*

- **antistasi_template_checker** *0.1.1*

- **arrow** *0.17.0*

- **async_property** *0.2.1*

- **asyncstdlib** *3.9.0*

- **beautifulsoup4** *4.9.3*

- **click** *7.1.2*

- **cryptography** *3.3.1*

- **dateparser** *1.0.0*

- **discord-flags** *2.1.1*

- **dpytest** *0.0.22*

- **emoji** *1.1.0*

- **fuzzywuzzy** *0.18.0*

- **gidappdata** *0.1.13*

- **gidconfig** *0.1.16*

- **gidlogger** *0.1.9*

- **googletrans** *4.0.0rc1*

- **humanize** *3.2.0*

- **icecream** *2.0.0*

- **marshmallow** *3.10.0*

- **matplotlib** *3.3.3*

- **psutil** *5.8.0*

- **pyfiglet** *0.8.post1*

- **python_a2s** *1.3.0*

- **python_dotenv** *0.15.0*

- **pytz** *2020.5*

- **rich** *9.13.0*

- **tldextract** *3.1.0*

- **watchgod** *0.6*

- **webdavclient3** *3.14.5*


### External dependencies


- [Cairo](https://www.cairographics.org/)
    - __Windows__
        follow these instructions `https://github.com/tschoonj/GTK-for-Windows-Runtime-Environment-Installer`

    - __Unix__
        sudo apt-get install -y libcairo2-dev

- [Pango](https://pango.gnome.org/)
    - __Windows__
        Follow this `https://github.com/ImageMagick/pango`

    - __Unix__
        sudo apt-get install -y libsdl-pango-dev



---

## License

MIT

---

## Development



### Future Plans





---

## See also



### Links


- [Antistasi Website](https://a3antistasi.enjin.com/)

- [Antistasi Steam Workshop Items](https://steamcommunity.com/id/OfficialAntiStasiCommunity/myworkshopfiles/)

- [A3 Antistasi Official Discord Server](https://discord.gg/8WNsueDKf5)


