with top_users as (
  select UserId, UserIdPartition, COUNT(0) as NumComments from {{ ref('comments') }}
    group by UserId, UserIdPartition order by NumComments desc limit {{ var('num_top_commenters', default=3) }}
),
user_info as (
  select * from {{ ref('users') }}
)
select user_info.*, NumComments
  from user_info
  inner join top_users
  on(user_info.Id = top_users.UserId and user_info.UserIdPartition = top_users.UserIdPartition)
  order by NumComments desc
