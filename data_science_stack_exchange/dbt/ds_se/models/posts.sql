select
  * except(CreationDate, LastEditDate, LastActivityDate, ClosedDate, CommunityOwnedDate),
  timestamp_micros(div(CreationDate, 1000)) as CreationDatetime,
  timestamp_micros(div(LastEditDate, 1000)) as LastEditDatetime,
  timestamp_micros(div(LastActivityDate, 1000)) as LastActivityDatetime,
  timestamp_micros(div(ClosedDate, 1000)) as ClosedDatetime,
  timestamp_micros(div(CommunityOwnedDate, 1000)) as CommunityOwnedDatetime
  from {{ source('stack_exchange', 'posts_external') }}
