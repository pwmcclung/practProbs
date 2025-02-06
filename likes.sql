SELECT
    LEAST(ul1.liker_id, ul1.liked_id) AS user1_id,
    GREATEST(ul1.liker_id, ul1.liked_id) AS user2_id
FROM
    user_likes ul1
INNER JOIN
    user_likes ul2 ON ul1.liker_id = ul2.liked_id AND ul1.liked_id = ul2.liker_id
WHERE ul1.liker_id < ul1.liked_id
GROUP BY user1_id, user2_id
ORDER BY user1_id, user2_id;