# MySQL advanced

> This project was andvanced MySQL concepts.

## Summary

I learnt about how to create tables with constraints, how to optimize queries by adding indexes, what is and how to implement stored procedures and functions in MySQL, what is and how to implement views in MySQL, and what is and how to implement triggers in MySQL.

## Files

> Each file contains the solution to a task in the project.

- [x] [0-uniq_users.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/0-uniq_users.sql): An SQL script that creates a table `users` following these requirements:
    - With these attributes:
      - `id`, integer, never null, auto increment and primary key
      - `email`, string (255 characters), never null and unique
      - `name`, string (255 characters)
- [x] [1-country_users.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/1-country_users.sql): An SQL script that creates a table `users` following these requirements:
    - With these attributes:
      - `id`, integer, never null, auto increment and primary key
      - `email`, string (255 characters), never null and unique
      - `name`, string (255 characters)
      - `country`, enumeration of countries: `US`, `CO` and `TN`, never null (= default will be the first element of the enumeration, here `US`)
- [x] [2-fans.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/2-fans.sql): An SQL script that ranks country origins of bands, ordered by the number of (non-unique) fans.
  - Import this table dump: [metal_bands.sql](./metal_bands.sql)
  - Column names must be: origin and nb_fans
- [x] [3-glam_rock.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/3-glam_rock.sql): An SQL script that lists all bands with `Glam rock` as their main style, ranked by their longevity.
- [x] [4-store.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/4-store.sql): An SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
- [x] [5-valid_email.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/5-valid_email.sql): An SQL script that creates a trigger that resets the attribute `valid_email` only when the `email` has been changed.
- [x] [6-bonus.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/6-bonus.sql): An SQL script that creates a stored procedure `AddBonus` that adds a new correction for a student.
- [x] [7-average_score.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/7-average_score.sql): An SQL script that creates a stored procedure `ComputeAverageScoreForUser` that computes and store the average score for a student.
- [x] [8-index_my_names.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/8-index_my_names.sql): An SQL script that creates an index `idx_name_first` on the table `names` and the first letter of `name`.
  - Import this table dump: [names.sql](./names.sql)
  - Only the first letter of `name` AND `score` must be indexed
- [x] [9-index_name_score.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/9-index_name_score.sql): An SQL script that creates an index `idx_name_first_score` on the table names and the first letter of `name` and the `score`.
  - Import this table dump: [names.sql](./names.sql)
  - Only the first letter of `name` AND `score` must be indexed
- [ ] [10-div.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/10-div.sql): An SQL script that creates a function `SafeDiv` that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0.
- [ ] [11-need_meeting.sql](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/11-need_meeting.sql): An SQL script that creates a view `need_meeting` that lists all students that have a score under 80 (strict) and no `last_meeting` or more than 1 month.
- [ ] [](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/):
- [ ] [](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x00-MySQL_Advanced/):

> [test_files](): A folder of test files. Provided by Alx.
