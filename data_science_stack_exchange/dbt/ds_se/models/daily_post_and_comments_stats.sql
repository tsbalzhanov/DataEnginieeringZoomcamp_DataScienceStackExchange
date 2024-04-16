with
  post_stats as (
    select
      CreationDate, count(0) AS NumPosts
      from (
        select
          date(CreationDatetime) AS CreationDate
          from {{ ref('posts') }}
    ) group by CreationDate
  ),
  comment_stats as (
    select
      CreationDate, count(0) AS NumComments
      from (
        select
          date(CreationDatetime) AS CreationDate
          from {{ ref('comments') }}
    ) group by CreationDate
  )
select *
  from comment_stats
  full join post_stats
  using (CreationDate)
  order by CreationDate
