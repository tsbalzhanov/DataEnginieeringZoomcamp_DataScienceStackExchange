with votes as (
  select VoteTypeId, COUNT(0) AS NumVotes from {{ ref('votes') }} group by VoteTypeId
),
vote_types as (
  select * from {{ ref('vote_types') }}
)
select vote_types.Name as VoteTypeName, votes.*
  from vote_types
  inner join votes
  on (vote_types.id = votes.VoteTypeId)
