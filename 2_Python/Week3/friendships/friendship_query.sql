SELECT friendships.id, users.first_name as User_1_First_Name, users.last_name as User_1_Last_Name, users2.first_name as User_2_First_Name, users2.last_name as User_2_Last_Name
FROM users 
JOIN friendships 
ON users.id = friendships.user_id 
JOIN users as users2 
ON users2.id = friendships.friend_id 
