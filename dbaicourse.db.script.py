
--22
SELECT e.winner FROM  eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE e.country LIKE 'Israel' ORDER BY e.YEAR DESC LIMIT 1
Netta
-------------------------------------------------------
--21
SELECT count(*)  FROM (SELECT DISTINCT s.genre FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR)
8
-----------------------------------------------
--20
SELECT e.song_name, s.language FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE s.LANGUAGE <> "English"
Refrain	French
Net als toen	Dutch
Dors mon amour	French
Een beetje	Dutch
Tom Pillibi	French
Nous les amoureux	French
Un premier amour	French
Dansevise	Danish
Non ho leta	Italian
-------------------------------------------------------
--19
SELECT e.country, avg(s.song_length_seconds) FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR GROUP BY e.country
Israel	178.75
Italy	173.33333333333334
Latvia	185.0
Luxembourg	184.0
Monaco	180.0
Netherlands	172.5
Norway	176.66666666666666
Portugal	175.0
Russia	180.0
Serbia	180.0
----------------------------------------------------
--18
SELECT e.song_name FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE s.solo_performance = TRUE ORDER BY s.song_length_seconds LIMIT 1
Puppet on a String
--------------------------------------------
--17
SELECT e.country FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE  s.song_length_seconds > (SELECT AVG(song_length_seconds) FROM SONG_DETAILS)
Switzerland
Netherlands
France
France
Luxembourg
France
Denmark
Austria
Spain
-------------------------------------------------
--16
SELECT e.song_name, e.country, e.YEAR, s.song_length_seconds  FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR ORDER BY song_length_seconds DESC
Un premier amour	France	1962	210
Merci Cherie	Austria	1966	200
Dors mon amour	France	1958	195
------------------------------------------------------
--15
SELECT MAX(e.year) FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE e.country LIKE 'Israel'
2018
------------------------------------------------------------
--15
SELECT min(e.year) FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE e.country LIKE 'Israel'
1978
-------------------------------------------------------------
--14
SELECT * FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR WHERE s.language = 'French'
1956	Switzerland	Lys Assia	Switzerland	Refrain
1958	France	Andre Claveau	Netherlands	Dors mon amour
1960	France	Jacqueline Boyer	United Kingdom	Tom Pillibi
--------------------------------------------------------
--13
SELECT  country, COUNT(*) AS wins FROM eurovision_winners GROUP BY country ORDER BY wins DESC
--12
SELECT  country, COUNT(*) AS win_count FROM eurovision_winners GROUP BY country ORDER BY win_count DESC LIMIT 1;
Sweden	7
-------------------------------
--11
SELECT e.song_name FROM song_details s RIGHT JOIN eurovision_winners e ON s.YEAR = e.YEAR WHERE S.song_length_seconds = (SELECT  max(song_length_seconds) FROM SONG_DETAILS)
Un premier amour
--------------------------------------------------
--11
SELECT max(song_length_seconds) FROM song_details s RIGHT JOIN eurovision_winners e ON s.YEAR = e.YEAR
210
-------------------------------------
--10
SELECT min(s.YEAR) FROM song_details s RIGHT JOIN eurovision_winners e ON s.YEAR = e.year  WHERE s.solo_performance = FALSE
1963
-----------------------------------------
--9
SELECT YEAR FROM eurovision_winners WHERE song_name = "Hallelujah"
1979
----------------------------------------
--8
SELECT avg(song_length_seconds) FROM song_details
179.26470588235293
--------------------------------------------------
--7
SELECT count(*) FROM eurovision_winners e  inner JOIN song_details s ON e.YEAR = s.YEAR WHERE s.LANGUAGE = "English"
37
-------------------------------------------------
--6
SELECT e.song_name FROM eurovision_winners e JOIN song_details s ON e.YEAR = s.YEAR WHERE s.solo_performance = TRUE
Refrain
Net als toen
Dors mon amour
Een beetje
Tom Pillibi
Nous les amoureux
Un premier amour
Non ho leta
Poupee de cire poupee de son
Merci Cherie
Puppet on a String
La la la
All Kinds of Everything
Un banc un arbre une rue
Apres toi
Tu te reconnaitras
Loiseau et lenfant
Whats Another Year
Ein bisschen Frieden
Si la vie est cadeau
Jaime la vie
Hold Me Now
Ne partez pas sans moi
Insieme 1992
Fangad av en stormvind
Why Me
In Your Eyes
The Voice
Diva
Take Me to Your Heaven
I Wanna
Everyway That I Can
My Number One
Molitva
Believe
Fairytale
Satellite
Euphoria
Only Teardrops
Rise Like a Phoenix
Heroes
1944
Amar pelos dois
Toy
Arcade
Tattoo
The Code
--------------------------------------------
--5
SELECT * FROM eurovision_winners e  JOIN song_details s ON e.YEAR = s.YEAR
1956	Switzerland	Lys Assia	Switzerland	Refrain
1957	Netherlands	Corry Brokken	Germany	Net als toen
175	1 pop italian
175 1 pop French
--------------------------------------
--4
SELECT min(song_length_seconds) FROM song_details
160
--------------------------------------------
--3
SELECT YEAR FROM eurovision_winners WHERE country LIKE "israel"
1978
1979
1998
2018
-----------------------------------------
--2
SELECT count(*) FROM eurovision_winners WHERE country = host_country
6
-----------------------------------------------------
--1
SELECT count(*) FROM eurovision_winners WHERE country LIKE 'Israel'
4