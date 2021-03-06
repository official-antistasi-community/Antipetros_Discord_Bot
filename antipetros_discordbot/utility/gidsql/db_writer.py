# region [Imports]

# * Standard Library Imports ---------------------------------------------------------------------------->
import logging
import sqlite3 as sqlite
import textwrap
from typing import Union

# * Gid Imports ----------------------------------------------------------------------------------------->
import gidlogger as glog
import aiosqlite
# * Local Imports --------------------------------------------------------------------------------------->
from antipetros_discordbot.utility.gidsql.db_action_base import GidSqliteActionBase, AioGidSqliteActionBase

# endregion [Imports]

__updated__ = '2020-11-26 17:04:24'


# region [Logging]

log = logging.getLogger('gidsql')

glog.import_notification(log, __name__)

# endregion [Logging]


# region [Class_1]

class GidSQLiteWriter(GidSqliteActionBase):

    def __init__(self, in_db_loc, in_pragmas=None, log_execution: bool = True):
        super().__init__(in_db_loc, in_pragmas)
        self.log_execution = log_execution
        glog.class_init_notification(log, self)

    def write(self, sql_phrase: str, variables: Union[str, tuple, list] = None):
        conn = sqlite.connect(self.db_loc, isolation_level=None, detect_types=sqlite.PARSE_DECLTYPES)
        cursor = conn.cursor()
        try:
            self._execute_pragmas(cursor)
            if variables is not None:
                if isinstance(variables, str):
                    cursor.execute(sql_phrase, (variables,))
                    if self.log_execution is True:
                        _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                        _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                        log.debug("Executed sql phrase '%s' with args %s successfully", _log_sql_phrase, _log_args)
                elif isinstance(variables, tuple):
                    cursor.execute(sql_phrase, variables)
                    if self.log_execution is True:
                        _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                        _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                        log.debug("Executed sql phrase '%s' with args %s successfully", _log_sql_phrase, _log_args)
                elif isinstance(variables, list):
                    cursor.executemany(sql_phrase, variables)
                    if self.log_execution is True:
                        _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                        _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                        log.debug("ExecutedMany sql phrase from '%s' with arg-iterable %s successfully", _log_sql_phrase, _log_args)
            else:
                cursor.executescript(sql_phrase)
                if self.log_execution is True:
                    _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                    log.debug("ExecutedScript sql phrase '%s' successfully", _log_sql_phrase)
            conn.commit()
        except sqlite.Error as error:
            _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
            _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
            self._handle_error(error, _log_sql_phrase, _log_args)
        finally:
            conn.close()

    def create_aggregate(self, aggregate_name: str, num_params: int, aggregate_class):
        con = sqlite.connect(self.db_loc, isolation_level=None, detect_types=sqlite.PARSE_DECLTYPES)
        con.create_aggregate(aggregate_name, num_params, aggregate_class)
        con.close()

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.db_loc}')"

    def __str__(self):
        return self.__class__.__name__
# endregion [Class_1]


class AioGidSQLiteWriter(AioGidSqliteActionBase):
    def __init__(self, in_db_loc, in_pragmas=None, log_execution: bool = True):
        super().__init__(in_db_loc, in_pragmas)
        self.log_execution = log_execution
        glog.class_init_notification(log, self)

    async def write(self, sql_phrase: str, variables: Union[str, tuple, list] = None):
        # isolation_level=None
        async with aiosqlite.connect(self.db_loc, detect_types=sqlite.PARSE_DECLTYPES) as conn:

            try:
                await self._execute_pragmas(conn)
                if variables is not None:
                    if isinstance(variables, str):
                        await conn.execute(sql_phrase, (variables,))
                        if self.log_execution is True:
                            _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                            _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                            log.debug("Executed sql phrase '%s' with args %s successfully", _log_sql_phrase, _log_args)
                    elif isinstance(variables, tuple):
                        await conn.execute(sql_phrase, variables)
                        if self.log_execution is True:
                            _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                            _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                            log.debug("Executed sql phrase '%s' with args %s successfully", _log_sql_phrase, _log_args)
                    elif isinstance(variables, list):
                        await conn.executemany(sql_phrase, variables)
                        if self.log_execution is True:
                            _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                            _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                            log.debug("ExecutedMany sql phrase from '%s' with arg-iterable %s successfully", _log_sql_phrase, _log_args)
                else:
                    await conn.executescript(sql_phrase)
                    if self.log_execution is True:
                        _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                        log.debug("ExecutedScript sql phrase '%s' successfully", _log_sql_phrase)
                await conn.commit()
            except sqlite.Error as error:
                _log_sql_phrase = ' '.join(sql_phrase.replace('\n', ' ').split())
                _log_args = textwrap.shorten(str(variables), width=200, placeholder='...')
                await self._handle_error(error, _log_sql_phrase, _log_args)

    async def create_aggregate(self, aggregate_name: str, num_params: int, aggregate_class):
        con = await aiosqlite.connect(self.db_loc, isolation_level=None, detect_types=sqlite.PARSE_DECLTYPES)
        await con.create_aggregate(aggregate_name, num_params, aggregate_class)
        await con.close()

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.db_loc}')"

    def __str__(self):
        return self.__class__.__name__


if __name__ == '__main__':
    pass
