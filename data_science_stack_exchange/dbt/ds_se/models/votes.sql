select
  * except(CreationDate),
  timestamp_micros(div(CreationDate, 1000)) as CreationDatetime
  from {{ source('stack_exchange', 'votes_external') }}
