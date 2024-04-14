select
  * except(CreationDate, LastAccessDate),
  timestamp_micros(div(CreationDate, 1000)) as CreationDatetime,
  timestamp_micros(div(LastAccessDate, 1000)) as LastAccessDatetime
  from {{ source('stack_exchange', 'users_external') }}
