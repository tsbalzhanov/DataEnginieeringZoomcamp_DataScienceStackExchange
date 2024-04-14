with top_users as (
  select OwnerUserId, UserIdPartition, COUNT(0) as NumPosts from {{ ref('posts') }}
    group by OwnerUserId, UserIdPartition order by NumPosts desc limit {{ var('num_top_posters', default=3) }}
),
user_info as (
  select * from {{ ref('users') }}
)
select user_info.*, NumPosts
  from user_info
  inner join top_users
  on(user_info.Id = top_users.OwnerUserId and user_info.UserIdPartition = top_users.UserIdPartition)
  order by NumPosts desc
