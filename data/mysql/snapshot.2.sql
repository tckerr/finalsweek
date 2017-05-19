# ************************************************************
# Sequel Pro SQL dump
# Version 4096
#
# http://www.sequelpro.com/
# http://code.google.com/p/sequel-pro/
#
# Host: 127.0.0.1 (MySQL 5.6.23)
# Database: finalsweek
# Generation Time: 2017-05-18 21:49:43 +0000
# ************************************************************


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table account_emailaddress
# ------------------------------------------------------------

DROP TABLE IF EXISTS `account_emailaddress`;

CREATE TABLE `account_emailaddress` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `email` varchar(254) NOT NULL,
  `verified` tinyint(1) NOT NULL,
  `primary` tinyint(1) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  KEY `account_emailaddress_user_id_2c513194_fk_auth_user_id` (`user_id`),
  CONSTRAINT `account_emailaddress_user_id_2c513194_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `account_emailaddress` WRITE;
/*!40000 ALTER TABLE `account_emailaddress` DISABLE KEYS */;

INSERT INTO `account_emailaddress` (`id`, `email`, `verified`, `primary`, `user_id`)
VALUES
	(1,'tckerr@gmail.com',0,1,2),
	(2,'tckerr3@gmail.com',0,1,3),
	(3,'tckerr4@gmail.com',0,1,4),
	(4,'aaa@aaa.com',0,1,5),
	(5,'aaa2@aaa.com',0,1,6),
	(6,'asdjkl@askdjasd.com',0,1,7),
	(7,'gabbagabba345345345345@gmail.com',0,1,8),
	(8,'abcasdasd@abcasdasd.com',0,1,9);

/*!40000 ALTER TABLE `account_emailaddress` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table account_emailconfirmation
# ------------------------------------------------------------

DROP TABLE IF EXISTS `account_emailconfirmation`;

CREATE TABLE `account_emailconfirmation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `sent` datetime(6) DEFAULT NULL,
  `key` varchar(64) NOT NULL,
  `email_address_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `key` (`key`),
  KEY `account_ema_email_address_id_5b7f8c58_fk_account_emailaddress_id` (`email_address_id`),
  CONSTRAINT `account_ema_email_address_id_5b7f8c58_fk_account_emailaddress_id` FOREIGN KEY (`email_address_id`) REFERENCES `account_emailaddress` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_group
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_group_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_84c5c92e_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_permission
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_2f476e4b_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`)
VALUES
	(1,'Can add log entry',1,'add_logentry'),
	(2,'Can change log entry',1,'change_logentry'),
	(3,'Can delete log entry',1,'delete_logentry'),
	(4,'Can add group',2,'add_group'),
	(5,'Can change group',2,'change_group'),
	(6,'Can delete group',2,'delete_group'),
	(7,'Can add user',3,'add_user'),
	(8,'Can change user',3,'change_user'),
	(9,'Can delete user',3,'delete_user'),
	(10,'Can add permission',4,'add_permission'),
	(11,'Can change permission',4,'change_permission'),
	(12,'Can delete permission',4,'delete_permission'),
	(13,'Can add content type',5,'add_contenttype'),
	(14,'Can change content type',5,'change_contenttype'),
	(15,'Can delete content type',5,'delete_contenttype'),
	(16,'Can add session',6,'add_session'),
	(17,'Can change session',6,'change_session'),
	(18,'Can delete session',6,'delete_session'),
	(19,'Can add Token',7,'add_token'),
	(20,'Can change Token',7,'change_token'),
	(21,'Can delete Token',7,'delete_token'),
	(25,'Can add card type',9,'add_cardtype'),
	(26,'Can change card type',9,'change_cardtype'),
	(27,'Can delete card type',9,'delete_cardtype'),
	(52,'Can add student info',18,'add_studentinfo'),
	(53,'Can change student info',18,'change_studentinfo'),
	(54,'Can delete student info',18,'delete_studentinfo'),
	(55,'Can add card',19,'add_card'),
	(56,'Can change card',19,'change_card'),
	(57,'Can delete card',19,'delete_card'),
	(88,'Can add game',30,'add_game'),
	(89,'Can change game',30,'change_game'),
	(90,'Can delete game',30,'delete_game'),
	(91,'Can add participant',31,'add_participant'),
	(92,'Can change participant',31,'change_participant'),
	(93,'Can delete participant',31,'delete_participant'),
	(94,'Can add mutation effect',32,'add_mutationeffect'),
	(95,'Can change mutation effect',32,'change_mutationeffect'),
	(96,'Can delete mutation effect',32,'delete_mutationeffect'),
	(100,'Can add mutation template',34,'add_mutationtemplate'),
	(101,'Can change mutation template',34,'change_mutationtemplate'),
	(102,'Can delete mutation template',34,'delete_mutationtemplate'),
	(103,'Can add operation modifier',32,'add_operationmodifier'),
	(104,'Can change operation modifier',32,'change_operationmodifier'),
	(105,'Can delete operation modifier',32,'delete_operationmodifier'),
	(106,'Can add operation tag',35,'add_operationtag'),
	(107,'Can change operation tag',35,'change_operationtag'),
	(108,'Can delete operation tag',35,'delete_operationtag'),
	(109,'Can add site',36,'add_site'),
	(110,'Can change site',36,'change_site'),
	(111,'Can delete site',36,'delete_site'),
	(112,'Can add email address',37,'add_emailaddress'),
	(113,'Can change email address',37,'change_emailaddress'),
	(114,'Can delete email address',37,'delete_emailaddress'),
	(115,'Can add email confirmation',38,'add_emailconfirmation'),
	(116,'Can change email confirmation',38,'change_emailconfirmation'),
	(117,'Can delete email confirmation',38,'delete_emailconfirmation');

/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`)
VALUES
	(1,'pbkdf2_sha256$30000$TC2TuVyBoN1N$Bdckr1vX4dlOj2/lS6wMreyZTVTaoZTPdSSStRym7Qs=','2017-05-18 12:35:44.026559',1,'tom','','','',1,1,'2017-04-08 20:27:40.976868'),
	(2,'pbkdf2_sha256$30000$GHjs69AraAt6$zGhhg+MrP4BZugIZ92DtFMnt/JpXHXXTxAa8xorAzZE=',NULL,0,'tom2','','','tckerr@gmail.com',0,1,'2017-05-08 01:44:02.989376'),
	(3,'pbkdf2_sha256$30000$LxVlPZrFc79n$5SLnyQM/+Fa20MD78hAcS/MPfoHVrIiU7+iW9oNlkPM=',NULL,0,'tom3','','','tckerr3@gmail.com',0,1,'2017-05-08 01:44:58.913551'),
	(4,'pbkdf2_sha256$30000$tYFjIBUsytC1$SD1dwi6Ff4RDrEGTE2L+VgRZ6v3ZXKo7E25eievi5Ag=','2017-05-08 01:45:56.696292',0,'tom4','','','tckerr4@gmail.com',0,1,'2017-05-08 01:45:56.627609'),
	(5,'pbkdf2_sha256$30000$zXZ2lVLBXBiT$UVRyGJKvIFN1ePk+dxcHoxJVEkXD1E85t3k2ZKeq6gI=','2017-05-08 01:51:53.239207',0,'aaa','','','aaa@aaa.com',0,1,'2017-05-08 01:51:53.076384'),
	(6,'pbkdf2_sha256$30000$rHRR1bqynoZ9$uYB/0ld7LZNZVMHW+/NUQvujGMos1JhZD4p601IrilA=','2017-05-08 01:53:46.570006',0,'aaa2','','','aaa2@aaa.com',0,1,'2017-05-08 01:53:35.505238'),
	(7,'pbkdf2_sha256$30000$jXxAbcVdRb4w$qdqjMDoV5Yhg1OJJKtEyxJ4NgRIieSlPAaHUYVAhQTY=','2017-05-08 01:54:41.580972',0,'askdj','','','asdjkl@askdjasd.com',0,1,'2017-05-08 01:54:41.507130'),
	(8,'pbkdf2_sha256$30000$Jw8O0MwdIwmg$ldJQX8+YZvM3KZgurTrEOMMjQRtvRztBgMhZESI2/W8=','2017-05-11 00:46:23.616142',0,'tk2','','','gabbagabba345345345345@gmail.com',0,1,'2017-05-11 00:46:15.215136'),
	(9,'pbkdf2_sha256$30000$wcEWFXZvumH9$ljbPtxNkn2U1lvwhjfZwwNndSRgyTxwtW/+aBU5vHgs=','2017-05-12 21:36:00.693960',0,'abcasdasd','','','abcasdasd@abcasdasd.com',0,1,'2017-05-12 21:36:00.610261');

/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table auth_user_groups
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table auth_user_user_permissions
# ------------------------------------------------------------

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_1fbb5f2c_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table authtoken_token
# ------------------------------------------------------------

DROP TABLE IF EXISTS `authtoken_token`;

CREATE TABLE `authtoken_token` (
  `key` varchar(40) NOT NULL,
  `created` datetime(6) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`key`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `authtoken_token_user_id_35299eff_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `authtoken_token` WRITE;
/*!40000 ALTER TABLE `authtoken_token` DISABLE KEYS */;

INSERT INTO `authtoken_token` (`key`, `created`, `user_id`)
VALUES
	('01b1474371659ad3424a89e2b1a600205b0f53be','2017-05-07 14:23:12.583680',1),
	('1c6a095085ead4a04a60a41c520fa118608fecd8','2017-05-08 01:51:53.194191',5),
	('2207be0673ccff80d7f7006f753f0133a052c29f','2017-05-08 01:45:56.659695',4),
	('5ef5d1bb451257715a984037cb5f14bb4e20c79b','2017-05-08 01:44:03.051980',2),
	('85b745bd250dd48ffb6249beb226caf305c843f2','2017-05-11 00:46:15.278367',8),
	('8b0ea46c541bfe6aec3701e876374e8c91b3173b','2017-05-08 01:53:35.567749',6),
	('a6c3d3ce068792ed02b624ab45c4f096fe1e816a','2017-05-08 01:44:58.993360',3),
	('e5cd378c63c65677f528c202d63c0ca072d95314','2017-05-08 01:54:41.569968',7),
	('f8606a2caf2315edb0630e4de342da48736f24e5','2017-05-12 21:36:00.679922',9);

/*!40000 ALTER TABLE `authtoken_token` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_admin_log
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_c4bce8eb_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`)
VALUES
	(1,'2017-04-08 20:28:28.969130','1','Requestor',1,'[{\"added\": {}}]',NULL,1),
	(2,'2017-04-08 20:28:39.130039','increase','increase',1,'[{\"added\": {}}]',NULL,1),
	(3,'2017-04-08 20:28:49.178874','decrease','decrease',1,'[{\"added\": {}}]',NULL,1),
	(4,'2017-04-08 20:30:11.503958','2','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(5,'2017-04-08 20:30:14.518745','1','Pop +10',1,'[{\"added\": {}}]',NULL,1),
	(6,'2017-04-08 20:30:31.646491','2','Grades -1',1,'[{\"added\": {}}]',NULL,1),
	(7,'2017-04-08 20:30:53.672757','1','Amount 1',1,'[{\"added\": {}}]',NULL,1),
	(8,'2017-04-08 20:31:06.328671','2','Amount 10',1,'[{\"added\": {}}]',NULL,1),
	(9,'2017-04-08 20:32:20.766423','1','Argue with Teacher (1)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Argue with Teacher (1) --> TARGETS Requestor --> WITH OPERATIONS Set: Pop +10\", \"name\": \"card target operation set\"}}]',19,1),
	(10,'2017-04-08 20:48:16.674222','1','Argue with Teacher (1)',2,'[]',19,1),
	(11,'2017-04-08 20:48:39.394303','1','Operation object',1,'[{\"added\": {}}]',NULL,1),
	(12,'2017-04-08 20:48:54.267821','1','Pop +amount',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(13,'2017-04-08 20:48:57.355017','1','Operation object',2,'[]',NULL,1),
	(14,'2017-04-08 20:55:48.098255','1','Pop +amount with args >> [<Argument: Amount 10>] (1)',2,'[]',NULL,1),
	(15,'2017-04-08 20:58:41.415363','2','Grades - amount',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(16,'2017-04-08 20:58:45.139744','2','Grades - amount with args >> [<Argument: Amount 1>] (2)',1,'[{\"added\": {}}]',NULL,1),
	(17,'2017-04-08 21:01:17.854828','2','-grades',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(18,'2017-04-08 21:01:26.519909','1','-pop',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(19,'2017-04-08 21:01:29.893658','2','-grades [\'Amount 1\']',2,'[]',NULL,1),
	(20,'2017-04-08 21:01:57.425987','2','10',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(21,'2017-04-08 21:02:03.384091','1','1',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(22,'2017-04-08 21:04:04.740508','3','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(23,'2017-04-08 21:04:47.577518','3','Joke (3)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"card target operation set\", \"object\": \"CARD Joke (3) --> TARGETS Requestor --> WITH OPERATIONS Set: \"}}]',19,1),
	(24,'2017-04-08 21:04:51.419407','3','Joke (3)',2,'[]',19,1),
	(25,'2017-04-08 21:05:45.519177','3','Same row/col student seat diff',1,'[{\"added\": {}}]',NULL,1),
	(26,'2017-04-08 21:06:03.845770','1','+pop',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(27,'2017-04-08 21:06:49.054638','3','Same row/col student seat diff *3',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(28,'2017-04-08 21:07:10.034682','3','+pop Same row/col student seat diff *3',1,'[{\"added\": {}}]',NULL,1),
	(29,'2017-04-08 21:27:09.183609','4','adjacent students count',1,'[{\"added\": {}}]',NULL,1),
	(30,'2017-04-08 21:31:19.975340','4','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(31,'2017-04-08 21:31:26.425990','4','+pop adjacent students count',1,'[{\"added\": {}}]',NULL,1),
	(32,'2017-04-08 21:32:13.137908','3','Pass Note (3)',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',19,1),
	(33,'2017-04-08 21:33:00.756623','5','Joke (5)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Joke (5) --> TARGETS Requestor --> WITH OPERATIONS Set: +pop adjacent students count\", \"name\": \"card target operation set\"}}]',19,1),
	(34,'2017-04-08 21:33:05.880901','5','Joke (5)',2,'[]',19,1),
	(35,'2017-04-08 21:34:59.708583','4','amount=adjacent students count',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(36,'2017-04-08 22:08:19.605769','4','amount=adjacent students count',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(37,'2017-04-08 22:09:18.245716','4','amount=adjacent students count',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(38,'2017-04-08 22:12:06.258459','4','amount=adjacent students count',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(39,'2017-04-08 22:18:18.336478','4','amount=adjacent students count',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(40,'2017-04-08 22:49:43.415319','2','\"Requestor if he/she has highest grades\"',1,'[{\"added\": {}}]',NULL,1),
	(41,'2017-04-08 22:49:49.368872','2','\"Requestor if he/she has highest grades',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(42,'2017-04-08 22:49:53.690109','2','Requestor if he/she has highest grades',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(43,'2017-04-08 22:50:28.523996','5','amount=amount +9',1,'[{\"added\": {}}]',NULL,1),
	(44,'2017-04-08 22:50:50.900128','5','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(45,'2017-04-08 22:50:53.971166','5','+pop amount +9',1,'[{\"added\": {}}]',NULL,1),
	(46,'2017-04-08 22:51:08.744998','5','amount=9',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',NULL,1),
	(47,'2017-04-08 22:51:38.176852','6','Dean\'s List (6)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Dean\'s List (6) --> TARGETS Requestor if he/she has highest grades --> WITH OPERATIONS Set: +pop 9\", \"name\": \"card target operation set\"}}]',19,1),
	(48,'2017-04-08 22:53:42.288051','2','Requestor if he/she has highest grades',2,'[{\"changed\": {\"fields\": [\"sift\"]}}]',NULL,1),
	(49,'2017-04-08 23:13:27.468923','7','Pay Attention (7)',1,'[{\"added\": {}}]',19,1),
	(50,'2017-04-08 23:13:38.482803','6','amount=4',1,'[{\"added\": {}}]',NULL,1),
	(51,'2017-04-08 23:13:52.107604','6','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(52,'2017-04-08 23:14:10.214996','3','+grades',1,'[{\"added\": {}}]',NULL,1),
	(53,'2017-04-08 23:14:13.153323','6','+grades 1',1,'[{\"added\": {}}]',NULL,1),
	(54,'2017-04-08 23:14:33.051455','7','Pay Attention (7)',2,'[{\"added\": {\"object\": \"CARD Pay Attention (7) --> TARGETS Requestor --> WITH OPERATIONS Set: +grades 1\", \"name\": \"card target operation set\"}}]',19,1),
	(55,'2017-04-08 23:14:53.670869','8','Tutor (8)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Tutor (8) --> TARGETS Requestor --> WITH OPERATIONS Set: +grades 1\", \"name\": \"card target operation set\"}}]',19,1),
	(56,'2017-04-08 23:15:33.099448','7','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(57,'2017-04-08 23:15:34.087192','7','+pop 4',1,'[{\"added\": {}}]',NULL,1),
	(58,'2017-04-08 23:15:51.844242','8','Tutor (8)',2,'[{\"added\": {\"object\": \"CARD Tutor (8) --> TARGETS Requestor --> WITH OPERATIONS Set: +pop 4\", \"name\": \"card target operation set\"}}]',19,1),
	(59,'2017-04-08 23:18:20.484958','3','Adjacent students',1,'[{\"added\": {}}]',NULL,1),
	(60,'2017-04-08 23:18:37.412834','7','amount=6',1,'[{\"added\": {}}]',NULL,1),
	(61,'2017-04-08 23:19:10.457437','8','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(62,'2017-04-08 23:19:25.615370','4','-pop',1,'[{\"added\": {}}]',NULL,1),
	(63,'2017-04-08 23:19:28.126346','8','-pop 6',1,'[{\"added\": {}}]',NULL,1),
	(64,'2017-04-08 23:20:36.318888','3','Single adjacent student',2,'[{\"changed\": {\"fields\": [\"description\", \"sift\"]}}]',NULL,1),
	(65,'2017-04-08 23:20:42.081226','9','Pull Out Chair (9)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Pull Out Chair (9) --> TARGETS Single adjacent student --> WITH OPERATIONS Set: -pop 6\", \"name\": \"card target operation set\"}}]',19,1),
	(66,'2017-04-08 23:38:12.771458','8','amount=2',1,'[{\"added\": {}}]',NULL,1),
	(67,'2017-04-08 23:38:32.303716','9','amount=3',1,'[{\"added\": {}}]',NULL,1),
	(68,'2017-04-08 23:41:40.189903','5','+trouble',1,'[{\"added\": {}}]',NULL,1),
	(69,'2017-04-08 23:41:48.877791','9','+trouble 3',1,'[{\"added\": {}}]',NULL,1),
	(70,'2017-04-08 23:42:30.177771','10','+trouble 4',1,'[{\"added\": {}}]',NULL,1),
	(71,'2017-04-08 23:45:07.660421','3','Set: +pop Same row/col student seat diff *3, +trouble 3',2,'[{\"added\": {\"name\": \"operation\", \"object\": \"+trouble 3\"}}]',NULL,1),
	(72,'2017-04-08 23:45:57.973999','9','Set: +trouble 2',1,'[{\"added\": {}}, {\"added\": {\"name\": \"operation\", \"object\": \"+trouble 2\"}}]',NULL,1),
	(73,'2017-04-08 23:46:03.100908','9','Pull Out Chair (9)',2,'[{\"added\": {\"name\": \"card target operation set\", \"object\": \"CARD Pull Out Chair (9) --> TARGETS Requestor --> WITH OPERATIONS Set: +trouble 2\"}}]',19,1),
	(74,'2017-04-08 23:47:15.914548','10','Set: -pop 2',1,'[{\"added\": {}}, {\"added\": {\"name\": \"operation\", \"object\": \"-pop 2\"}}]',NULL,1),
	(75,'2017-04-08 23:47:41.728733','6','-torment',1,'[{\"added\": {}}]',NULL,1),
	(76,'2017-04-08 23:47:44.020128','10','Set: -pop 2, -torment 1',2,'[{\"added\": {\"name\": \"operation\", \"object\": \"-torment 1\"}}]',NULL,1),
	(77,'2017-04-08 23:47:51.204588','10','Cry (10)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"card target operation set\", \"object\": \"CARD Cry (10) --> TARGETS Requestor --> WITH OPERATIONS Set: -pop 2, -torment 1\"}}]',19,1),
	(78,'2017-04-08 23:48:03.916402','10','Cry (10)',2,'[]',19,1),
	(79,'2017-04-08 23:53:55.501787','4','Single target student',1,'[{\"added\": {}}]',NULL,1),
	(80,'2017-04-08 23:54:06.500771','11','Principal\'s Office (11)',1,'[{\"added\": {}}, {\"added\": {\"name\": \"card target operation set\", \"object\": \"CARD Principal\'s Office (11) --> TARGETS Single target student --> WITH OPERATIONS Set: +trouble 2\"}}]',19,1),
	(81,'2017-04-08 23:54:36.958732','4','Single target student',2,'[{\"changed\": {\"fields\": [\"sift\"]}}]',NULL,1),
	(82,'2017-04-10 23:24:48.420644','10','amount=5',1,'[{\"added\": {}}]',NULL,1),
	(83,'2017-04-10 23:25:07.253472','11','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(84,'2017-04-10 23:25:11.476883','15','-pop 5',1,'[{\"added\": {}}]',NULL,1),
	(85,'2017-04-10 23:26:17.346560','7','+torment',1,'[{\"added\": {}}]',NULL,1),
	(86,'2017-04-10 23:26:21.740816','11','Set: -pop 5, +torment 1',2,'[{\"added\": {\"object\": \"+torment 1\", \"name\": \"operation\"}}]',NULL,1),
	(87,'2017-04-10 23:26:24.680233','12','Bully (12)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Bully (12) --> TARGETS Single adjacent student --> WITH OPERATIONS Set: -pop 5, +torment 1\", \"name\": \"card target operation set\"}}]',19,1),
	(88,'2017-04-10 23:27:23.424298','12','Set: +trouble 3',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+trouble 3\", \"name\": \"operation\"}}]',NULL,1),
	(89,'2017-04-10 23:27:46.448068','13','Set: -pop 4',1,'[{\"added\": {}}, {\"added\": {\"object\": \"-pop 4\", \"name\": \"operation\"}}]',NULL,1),
	(90,'2017-04-10 23:28:02.324467','13','Tattle Tale (13)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Tattle Tale (13) --> TARGETS Single target student --> WITH OPERATIONS Set: +trouble 3\", \"name\": \"card target operation set\"}}, {\"added\": {\"object\": \"CARD Tattle Tale (13) --> TARGETS Requestor --> WITH OPERATIONS Set: -pop 4\", \"name\": \"card target operation set\"}}]',19,1),
	(91,'2017-04-10 23:28:28.877015','14','Set: +trouble 5',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+trouble 5\", \"name\": \"operation\"}}]',NULL,1),
	(92,'2017-04-10 23:28:34.635687','12','Bully (12)',2,'[{\"added\": {\"object\": \"CARD Bully (12) --> TARGETS Requestor --> WITH OPERATIONS Set: +trouble 5\", \"name\": \"card target operation set\"}}]',19,1),
	(93,'2017-04-10 23:29:01.413372','8','-trouble',1,'[{\"added\": {}}]',NULL,1),
	(94,'2017-04-10 23:29:05.571692','13','Set: -pop 4, -trouble 1',2,'[{\"added\": {\"object\": \"-trouble 1\", \"name\": \"operation\"}}]',NULL,1),
	(95,'2017-04-10 23:29:10.233426','13','Tattle Tale (13)',2,'[]',19,1),
	(96,'2017-04-10 23:30:14.292710','15','Set: -grades 4',1,'[{\"added\": {}}, {\"added\": {\"object\": \"-grades 4\", \"name\": \"operation\"}}]',NULL,1),
	(97,'2017-04-10 23:30:29.394366','14','Unprepared (14)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Unprepared (14) --> TARGETS Single target student --> WITH OPERATIONS Set: -grades 4\", \"name\": \"card target operation set\"}}]',19,1),
	(98,'2017-04-10 23:31:23.376909','11','amount=12',1,'[{\"added\": {}}]',NULL,1),
	(99,'2017-04-10 23:31:30.922581','16','Set: ',1,'[{\"added\": {}}]',NULL,1),
	(100,'2017-04-10 23:31:32.227672','22','+grades 12',1,'[{\"added\": {}}]',NULL,1),
	(101,'2017-04-10 23:32:04.811395','16','Set: +grades 12, +trouble 5',2,'[{\"added\": {\"object\": \"+trouble 5\", \"name\": \"operation\"}}]',NULL,1),
	(102,'2017-04-10 23:32:09.632001','15','Steal Test (15)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Steal Test (15) --> TARGETS Requestor --> WITH OPERATIONS Set: +grades 12, +trouble 5\", \"name\": \"card target operation set\"}}]',19,1),
	(103,'2017-04-10 23:33:39.110943','17','Set: +grades 6, -pop 2',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+grades 6\", \"name\": \"operation\"}}, {\"added\": {\"object\": \"-pop 2\", \"name\": \"operation\"}}]',NULL,1),
	(104,'2017-04-10 23:33:43.528219','16','Ask Question (16)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Ask Question (16) --> TARGETS Requestor --> WITH OPERATIONS Set: +grades 6, -pop 2\", \"name\": \"card target operation set\"}}]',19,1),
	(105,'2017-04-10 23:36:02.458178','5','All students',1,'[{\"added\": {}}]',NULL,1),
	(106,'2017-04-10 23:36:50.418889','12','amount=8',1,'[{\"added\": {}}]',NULL,1),
	(107,'2017-04-10 23:36:55.975769','18','Set: +grades 8',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+grades 8\", \"name\": \"operation\"}}]',NULL,1),
	(108,'2017-04-10 23:37:11.747927','17','Group Project (17)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Group Project (17) --> TARGETS All students --> WITH OPERATIONS Set: +grades 8\", \"name\": \"card target operation set\"}}, {\"added\": {\"object\": \"CARD Group Project (17) --> TARGETS Requestor --> WITH OPERATIONS Set: +pop 4\", \"name\": \"card target operation set\"}}]',19,1),
	(109,'2017-04-10 23:38:06.203159','19','Set: -pop adjacent students count',1,'[{\"added\": {}}, {\"added\": {\"object\": \"-pop adjacent students count\", \"name\": \"operation\"}}]',NULL,1),
	(110,'2017-04-10 23:38:27.513289','20','Set: +grades 8, -pop adjacent students count',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+grades 8\", \"name\": \"operation\"}}, {\"added\": {\"object\": \"-pop adjacent students count\", \"name\": \"operation\"}}]',NULL,1),
	(111,'2017-04-10 23:38:39.067786','18','Shush (18)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Shush (18) --> TARGETS Requestor --> WITH OPERATIONS Set: +grades 8, -pop adjacent students count\", \"name\": \"card target operation set\"}}]',19,1),
	(112,'2017-04-10 23:39:44.450367','set','set',1,'[{\"added\": {}}]',NULL,1),
	(113,'2017-04-10 23:40:32.390302','21','Set: +pop 3, +trouble 2',1,'[{\"added\": {}}, {\"added\": {\"object\": \"+pop 3\", \"name\": \"operation\"}}, {\"added\": {\"object\": \"+trouble 2\", \"name\": \"operation\"}}]',NULL,1),
	(114,'2017-04-10 23:41:04.355000','9','set trouble',1,'[{\"added\": {}}]',NULL,1),
	(115,'2017-04-10 23:41:15.483780','22','Set: set trouble 1',1,'[{\"added\": {}}, {\"added\": {\"object\": \"set trouble 1\", \"name\": \"operation\"}}]',NULL,1),
	(116,'2017-04-10 23:43:08.407964','13','amount=Requestor trouble',1,'[{\"added\": {}}]',NULL,1),
	(117,'2017-04-10 23:43:12.080312','23','Set: set trouble Requestor trouble',1,'[{\"added\": {}}, {\"added\": {\"object\": \"set trouble Requestor trouble\", \"name\": \"operation\"}}]',NULL,1),
	(118,'2017-04-10 23:43:27.222258','19','Who Said That? (19)',1,'[{\"added\": {}}, {\"added\": {\"object\": \"CARD Who Said That? (19) --> TARGETS Requestor --> WITH OPERATIONS Set: +pop 3, +trouble 2\", \"name\": \"card target operation set\"}}, {\"added\": {\"object\": \"CARD Who Said That? (19) --> TARGETS All students --> WITH OPERATIONS Set: set trouble Requestor trouble\", \"name\": \"card target operation set\"}}]',19,1),
	(119,'2017-04-10 23:45:58.492729','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"description\", \"value\"]}}]',NULL,1),
	(120,'2017-04-10 23:50:55.238757','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(121,'2017-04-10 23:51:07.163930','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(122,'2017-04-10 23:51:35.820480','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(123,'2017-04-10 23:54:59.306430','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(124,'2017-04-10 23:55:09.566964','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(125,'2017-04-10 23:56:21.325594','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(126,'2017-04-11 00:01:07.521051','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(127,'2017-04-11 00:06:39.824328','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(128,'2017-04-11 00:07:21.407602','23','Set: +trouble requestor trouble',2,'[{\"changed\": {\"object\": \"+trouble requestor trouble\", \"name\": \"operation\", \"fields\": [\"instruction\"]}}]',NULL,1),
	(129,'2017-04-11 00:32:28.992011','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(130,'2017-04-11 00:36:03.581173','13','amount=requestor trouble',2,'[{\"changed\": {\"fields\": [\"value\"]}}]',NULL,1),
	(131,'2017-04-11 00:39:27.303675','33','set trouble requestor trouble',2,'[{\"changed\": {\"fields\": [\"instruction\"]}}]',NULL,1),
	(132,'2017-04-12 23:46:59.053924','12','Bully (12)',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(133,'2017-04-13 00:04:18.522558','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(134,'2017-04-13 00:05:52.920676','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a torment token.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(135,'2017-04-13 00:17:00.750649','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(136,'2017-04-13 00:17:21.988681','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(137,'2017-04-13 00:17:47.225351','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(138,'2017-04-13 00:18:23.871144','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(139,'2017-04-13 00:18:55.207267','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(140,'2017-04-13 00:19:25.468997','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"trouble_cost\"]}}]',19,1),
	(141,'2017-04-13 00:19:36.726117','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(142,'2017-04-13 00:19:52.688980','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(143,'2017-04-13 00:20:41.413899','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target student +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(144,'2017-04-13 00:21:24.866169','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(145,'2017-04-13 00:21:41.200023','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(146,'2017-04-13 00:22:00.920784','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(147,'2017-04-13 00:22:21.191352','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(148,'2017-04-13 00:26:14.640486','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(149,'2017-04-13 00:26:53.182870','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(150,'2017-04-13 00:27:20.882126','11','Principal\'s Office (11): Target student +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(151,'2017-04-13 00:27:36.399285','9','Pull Out Chair (9): Adjacent student -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(152,'2017-04-13 00:28:08.099088','9','Pull Out Chair (9): Adjacent student -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"trouble_cost\"]}}]',19,1),
	(153,'2017-04-14 23:19:11.484124','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(154,'2017-04-14 23:21:08.173397','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(155,'2017-04-14 23:27:27.800699','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(156,'2017-04-14 23:28:24.254499','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(157,'2017-04-14 23:29:53.663277','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(158,'2017-04-14 23:35:38.708971','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(159,'2017-04-15 00:02:29.845982','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(160,'2017-04-15 00:02:34.800888','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(161,'2017-04-15 00:08:54.971055','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(162,'2017-04-15 00:08:54.977499','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(163,'2017-04-15 00:08:54.983053','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(164,'2017-04-15 00:12:32.902828','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(165,'2017-04-15 00:43:22.468052','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(166,'2017-04-15 00:43:27.838692','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(167,'2017-04-15 00:53:39.243215','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(168,'2017-04-15 01:19:05.266752','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(169,'2017-04-15 01:20:28.606345','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(170,'2017-04-15 01:21:31.989376','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(171,'2017-04-15 01:21:39.408646','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(172,'2017-04-15 01:21:39.414662','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(173,'2017-04-15 01:21:39.426194','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(174,'2017-04-15 01:21:42.637110','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(175,'2017-04-15 01:43:46.342177','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(176,'2017-04-15 01:43:56.220616','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(177,'2017-04-15 01:43:56.227809','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(178,'2017-04-15 01:43:56.239311','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(179,'2017-04-15 01:43:56.244904','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(180,'2017-04-15 01:43:56.251859','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(181,'2017-04-15 01:45:52.243928','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(182,'2017-04-15 01:47:17.244637','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(183,'2017-04-15 01:47:41.185098','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(184,'2017-04-15 01:48:33.745171','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(185,'2017-04-15 01:50:40.588490','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(186,'2017-04-15 01:52:17.862550','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(187,'2017-04-15 01:57:42.654210','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(188,'2017-04-15 01:57:55.193291','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(189,'2017-04-15 01:58:38.701712','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(190,'2017-04-15 01:59:03.369379','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(191,'2017-04-15 02:07:06.228840','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(192,'2017-04-15 02:09:03.124122','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(193,'2017-04-15 02:09:32.129498','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(194,'2017-04-15 02:09:32.135637','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(195,'2017-04-15 02:09:32.141762','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(196,'2017-04-15 02:09:32.153833','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(197,'2017-04-15 02:09:32.161765','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(198,'2017-04-15 02:18:17.276349','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(199,'2017-04-15 02:29:00.261013','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',1,'[{\"added\": {}}]',19,1),
	(200,'2017-04-15 02:29:32.532157','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(201,'2017-04-15 02:40:07.466162','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',1,'[{\"added\": {}}]',19,1),
	(202,'2017-04-15 02:47:34.752096','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',1,'[{\"added\": {}}]',19,1),
	(203,'2017-04-15 02:47:54.981702','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(204,'2017-04-15 02:49:36.001238','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(205,'2017-04-15 02:49:36.008303','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(206,'2017-04-15 02:49:36.014289','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(207,'2017-04-15 02:49:36.019802','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(208,'2017-04-15 02:49:36.025318','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(209,'2017-04-15 02:56:33.911519','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(210,'2017-04-15 02:56:33.918532','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(211,'2017-04-15 02:56:33.925551','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(212,'2017-04-15 02:56:33.931093','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(213,'2017-04-15 02:56:33.936580','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(214,'2017-04-15 11:06:16.193163','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(215,'2017-04-15 11:06:53.220906','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(216,'2017-04-15 11:07:54.975192','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target student +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(217,'2017-04-15 11:09:05.024659','11','Principal\'s Office (11): Target student +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(218,'2017-04-15 11:19:36.802494','9','Pull Out Chair (9): Adjacent student -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(219,'2017-04-15 11:20:42.980764','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(220,'2017-04-15 11:20:58.541733','9','Pull Out Chair (9): Adjacent student -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(221,'2017-04-15 11:21:31.357841','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(222,'2017-04-15 11:22:32.590779','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(223,'2017-04-15 11:25:50.721034','9','Pull Out Chair (9): Adjacent student -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(224,'2017-04-15 11:28:24.583588','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(225,'2017-04-15 11:29:52.813696','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(226,'2017-04-15 11:30:22.932163','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(227,'2017-04-15 11:32:34.304290','23','Console (23): Trouble -2. Remove torment from target student.',1,'[{\"added\": {}}]',19,1),
	(228,'2017-04-15 11:38:29.012033','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',1,'[{\"added\": {}}]',19,1),
	(229,'2017-04-15 11:39:52.378767','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(230,'2017-04-15 11:43:08.131629','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',1,'[{\"added\": {}}]',19,1),
	(231,'2017-04-15 11:45:08.346537','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',1,'[{\"added\": {}}]',19,1),
	(232,'2017-04-15 11:47:43.681867','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',1,'[{\"added\": {}}]',19,1),
	(233,'2017-04-15 11:55:13.710492','28','Good Story (28): Move any two students to empty seats adjacent to you.',1,'[{\"added\": {}}]',19,1),
	(234,'2017-04-15 11:56:16.106634','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(235,'2017-04-15 12:01:49.661069','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',1,'[{\"added\": {}}]',19,1),
	(236,'2017-04-15 13:30:31.878949','1',' ',3,'',18,1),
	(237,'2017-04-15 13:32:32.367635','2','Polly Bleu',1,'[{\"added\": {}}]',18,1),
	(238,'2017-04-15 13:33:34.388140','3','Sid Devon',1,'[{\"added\": {}}]',18,1),
	(239,'2017-04-15 13:36:03.932120','4','Dave Devoix',1,'[{\"added\": {}}]',18,1),
	(240,'2017-04-15 13:41:31.332366','2','Polly Bleu',2,'[{\"changed\": {\"fields\": [\"fear_name\", \"fear_description\"]}}]',18,1),
	(241,'2017-04-15 14:35:36.983128','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(242,'2017-04-15 14:35:45.313333','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(243,'2017-04-15 14:43:22.311047','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(244,'2017-04-15 14:43:41.594134','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(245,'2017-04-15 14:44:10.178055','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(246,'2017-04-15 14:45:32.524930','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(247,'2017-04-15 14:45:53.722907','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(248,'2017-04-15 14:46:14.975936','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(249,'2017-04-15 14:46:32.950019','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(250,'2017-04-15 14:48:21.312434','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(251,'2017-04-15 14:49:04.715883','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(252,'2017-04-15 14:49:45.197578','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(253,'2017-04-15 14:51:24.931447','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(254,'2017-04-15 14:51:41.042700','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[]',19,1),
	(255,'2017-04-15 14:54:25.620537','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(256,'2017-04-15 14:54:38.154468','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(257,'2017-04-15 14:54:38.160617','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(258,'2017-04-15 14:54:38.169372','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(259,'2017-04-15 14:54:38.178556','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(260,'2017-04-15 14:54:38.194779','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(261,'2017-04-15 14:54:38.203966','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(262,'2017-04-15 14:54:38.213218','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(263,'2017-04-15 14:54:38.224437','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(264,'2017-04-15 14:55:15.465077','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(265,'2017-04-15 14:55:56.331589','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(266,'2017-04-15 14:56:50.258698','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(267,'2017-04-15 14:58:32.536983','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(268,'2017-04-15 14:59:18.059569','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(269,'2017-04-15 15:00:25.882909','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(270,'2017-04-15 15:00:34.412342','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(271,'2017-04-15 15:00:34.418159','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(272,'2017-04-15 15:00:34.423985','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(273,'2017-04-15 15:01:05.802000','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(274,'2017-04-15 15:01:05.809358','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(275,'2017-04-15 15:01:05.815245','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(276,'2017-04-15 15:01:05.820836','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(277,'2017-04-15 15:01:05.829473','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(278,'2017-04-15 15:02:12.688085','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(279,'2017-04-15 15:03:40.043105','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"description\", \"script\", \"active\"]}}]',19,1),
	(280,'2017-04-15 15:06:14.320966','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"description\", \"script\", \"active\"]}}]',19,1),
	(281,'2017-04-15 15:06:32.561987','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(282,'2017-04-15 15:06:58.198326','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(283,'2017-04-15 15:07:32.094773','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(284,'2017-04-15 15:08:03.139942','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(285,'2017-04-15 15:08:09.496675','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(286,'2017-04-15 15:08:09.502809','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(287,'2017-04-15 15:08:09.509138','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(288,'2017-04-15 15:08:09.514978','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(289,'2017-04-15 15:08:09.525994','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(290,'2017-04-15 15:08:09.532341','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(291,'2017-04-15 15:11:41.554101','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"description\", \"script\", \"active\"]}}]',19,1),
	(292,'2017-04-15 15:12:37.005832','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(293,'2017-04-15 15:12:43.366763','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"trouble_cost\"]}}]',19,1),
	(294,'2017-04-15 15:13:03.791040','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(295,'2017-04-15 15:13:20.453639','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(296,'2017-04-15 15:14:18.879964','14','Unprepared (14): Target student -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(297,'2017-04-15 15:14:27.859138','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(298,'2017-04-15 15:14:57.280188','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(299,'2017-04-15 15:15:31.104821','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(300,'2017-04-15 15:18:39.097470','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(301,'2017-04-15 15:22:50.624834','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(302,'2017-04-15 15:33:30.579187','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(303,'2017-04-15 15:35:24.055009','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(304,'2017-04-15 15:36:13.250971','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(305,'2017-04-15 15:36:29.251198','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(306,'2017-04-22 16:30:50.534555','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(307,'2017-04-27 00:28:02.012231','3','double (3)',1,'[{\"added\": {}}]',32,1),
	(308,'2017-04-27 00:43:41.128196','3','double (3)',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',32,1),
	(309,'2017-04-27 01:41:19.241902','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(310,'2017-04-27 01:41:19.248059','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(311,'2017-04-27 01:41:19.253923','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(312,'2017-04-27 01:41:19.259919','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(313,'2017-04-27 01:41:19.268100','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(314,'2017-04-27 01:41:19.275443','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(315,'2017-04-27 01:41:19.283262','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(316,'2017-04-27 01:41:19.290771','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(317,'2017-04-27 01:41:19.298332','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(318,'2017-04-27 01:41:19.306693','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(319,'2017-04-27 01:41:19.314828','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(320,'2017-04-27 01:41:19.322519','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(321,'2017-04-27 01:41:19.330535','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(322,'2017-04-27 01:41:19.338550','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(323,'2017-04-27 01:41:19.346565','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(324,'2017-04-27 01:41:19.354659','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(325,'2017-04-27 01:41:19.361567','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(326,'2017-04-27 01:41:19.368503','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(327,'2017-04-27 01:41:19.376440','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(328,'2017-04-27 01:41:19.384065','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(329,'2017-04-27 01:41:19.394091','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(330,'2017-04-27 01:41:19.400960','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(331,'2017-04-27 01:41:19.410082','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(332,'2017-04-27 01:41:19.418105','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(333,'2017-04-27 01:41:19.425630','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(334,'2017-04-27 01:41:19.433706','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(335,'2017-04-27 01:45:32.817691','30','Mutation Test (30): A test for mutations',1,'[{\"added\": {}}]',19,1),
	(336,'2017-04-27 22:32:13.117254','1','MutationExpiryCriteria object',1,'[{\"added\": {}}]',NULL,1),
	(337,'2017-04-28 20:29:29.511622','System','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(338,'2017-04-28 20:29:41.548097','ActorAction','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(339,'2017-04-28 20:29:49.687977','StatusEffect','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(340,'2017-04-28 20:29:58.000717','AutomaticEffect','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(341,'2017-04-28 20:30:25.663458','Card','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(342,'2017-04-28 20:30:33.399858','DisciplineCard','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(343,'2017-04-28 20:30:42.126123','AfterSchoolCard','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(344,'2017-04-28 20:30:50.573305','ActionCard','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(345,'2017-04-28 20:30:56.236702','PlayedCard','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(346,'2017-04-28 20:31:09.010239','AutomaticCard','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(347,'2017-04-28 20:31:19.297152','AfterSchoolCardCost','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(348,'2017-04-28 20:31:24.740574','CardCost','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(349,'2017-04-28 20:31:34.356607','ProximateEffect','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(350,'2017-04-28 20:31:41.476773','OnDraw','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(351,'2017-04-28 20:31:48.773278','TurnBound','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(352,'2017-04-28 20:31:56.724842','PhaseBound','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(353,'2017-04-28 20:32:06.684709','StageBound','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(354,'2017-04-28 20:32:40.354441','UseBound','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(355,'2017-04-28 20:32:56.472409','UntilRemoved','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(356,'2017-04-28 20:33:13.050019','{{[][[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\'=]\'\'','OperationTag object',1,'[{\"added\": {}}]',35,1),
	(357,'2017-04-28 20:34:10.134373','Permanent','Permanent',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',35,1),
	(358,'2017-04-28 20:34:21.083223','Popularity','Popularity',1,'[{\"added\": {}}]',35,1),
	(359,'2017-04-28 20:34:27.436656','Grades','Grades',1,'[{\"added\": {}}]',35,1),
	(360,'2017-04-28 20:34:34.061763','Trouble','Trouble',1,'[{\"added\": {}}]',35,1),
	(361,'2017-04-28 20:34:40.333227','Torment','Torment',1,'[{\"added\": {}}]',35,1),
	(362,'2017-04-28 20:35:29.087496','{{[][[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\'=]\'\'','{{[][[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[[\'=]\'\'',3,'',35,1),
	(363,'2017-04-28 21:11:11.146233','30','Mutation Test (30): A test for mutations',3,'',19,1),
	(364,'2017-04-28 21:23:21.600443','1','MutationTemplate object',1,'[{\"added\": {}}]',34,1),
	(365,'2017-04-28 21:23:23.964224','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"mutation_template\"]}}]',19,1),
	(366,'2017-04-28 22:27:31.144835','1','Standard Action Card',2,'[{\"changed\": {\"fields\": [\"name\", \"tags\"]}}]',34,1),
	(367,'2017-04-28 22:29:28.868157','1','Standard Action Card',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',34,1),
	(368,'2017-04-28 22:29:31.166564','1','Standard Action Card',2,'[]',34,1),
	(369,'2017-04-28 22:51:54.169925','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"mutation_template\"]}}]',19,1),
	(370,'2017-04-28 22:52:00.786267','7','Pay Attention (7): +4 Grades.',2,'[]',19,1),
	(371,'2017-04-28 23:02:21.992994','2','Double All Grades',1,'[{\"added\": {}}]',34,1),
	(372,'2017-04-28 23:04:03.760444','2','Double All Grades Permanently',2,'[{\"changed\": {\"fields\": [\"name\", \"tags\"]}}]',34,1),
	(373,'2017-04-28 23:04:31.512673','31','Mutation Test (31): Mutation test',1,'[{\"added\": {}}]',19,1),
	(374,'2017-04-28 23:05:42.119988','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(375,'2017-04-28 23:19:29.499415','31','Mutation Test (31): Mutation test',2,'[]',19,1),
	(376,'2017-04-28 23:19:37.777008','31','Mutation Test (31): Mutation test',2,'[]',19,1),
	(377,'2017-04-28 23:19:41.996053','7','Pay Attention (7): +4 Grades.',2,'[]',19,1),
	(378,'2017-04-29 00:03:19.909225','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(379,'2017-04-29 00:03:19.916745','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(380,'2017-04-29 00:03:19.922910','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(381,'2017-04-29 00:18:35.196531','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(382,'2017-04-29 00:18:50.809242','double','double',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',32,1),
	(383,'2017-04-29 00:20:58.098833','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(384,'2017-04-29 00:21:41.421585','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(385,'2017-04-29 00:25:20.431479','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(386,'2017-04-29 00:28:54.716966','double','double',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',32,1),
	(387,'2017-04-29 00:45:29.569870','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(388,'2017-04-29 00:45:29.575915','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(389,'2017-04-29 00:45:29.581902','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(390,'2017-04-29 01:05:55.463885','floor_0','floor_0',1,'[{\"added\": {}}]',32,1),
	(391,'2017-04-29 01:06:05.518714','3','0 trouble on next action',1,'[{\"added\": {}}]',34,1),
	(392,'2017-04-29 01:06:56.232373','32','Distract Teacher (32): Generate 0 Trouble on your next action.',1,'[{\"added\": {}}]',19,1),
	(393,'2017-04-29 01:24:09.660468','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',34,1),
	(394,'2017-04-29 01:24:14.661238','32','Distract Teacher (32): Generate 0 Trouble on your next action.',2,'[]',19,1),
	(395,'2017-04-29 01:36:33.220917','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"uses\"]}}]',34,1),
	(396,'2017-04-29 01:37:27.128394','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(397,'2017-04-29 01:37:42.508669','31','Mutation Test (31): Mutation test',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(398,'2017-04-29 01:37:42.514891','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(399,'2017-04-29 01:37:42.521747','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(400,'2017-04-29 01:37:42.529729','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(401,'2017-04-29 01:37:42.537593','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(402,'2017-04-29 01:53:38.945720','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',34,1),
	(403,'2017-04-29 02:00:06.999047','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(404,'2017-04-29 02:00:07.004978','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(405,'2017-04-29 02:00:07.010492','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(406,'2017-04-29 02:00:07.016088','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(407,'2017-04-29 02:00:07.021677','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(408,'2017-04-29 02:00:07.027168','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(409,'2017-04-29 02:00:07.032176','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(410,'2017-04-29 02:00:07.037741','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(411,'2017-04-29 02:00:07.043955','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(412,'2017-04-29 02:00:07.049587','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(413,'2017-04-29 02:00:07.055178','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(414,'2017-04-29 02:00:07.060374','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(415,'2017-04-29 02:00:07.065905','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(416,'2017-04-29 02:00:07.070904','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(417,'2017-04-29 02:00:07.076008','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(418,'2017-04-29 02:00:07.081416','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(419,'2017-04-29 02:00:07.086518','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(420,'2017-04-29 02:00:07.091513','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(421,'2017-04-29 02:00:07.096976','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(422,'2017-04-29 02:00:07.102490','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(423,'2017-04-29 02:00:07.109029','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(424,'2017-04-29 02:00:07.114716','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(425,'2017-04-29 02:00:07.120563','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(426,'2017-04-29 02:00:07.126068','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(427,'2017-04-29 02:00:07.132739','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(428,'2017-04-29 02:00:07.138923','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(429,'2017-04-29 10:01:16.450016','4','double grades next action',1,'[{\"added\": {}}]',34,1),
	(430,'2017-04-29 10:37:04.854998','4','double grades next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(431,'2017-04-29 10:37:11.168655','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(432,'2017-04-29 10:39:10.768150','2','Double All Grades Permanently',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(433,'2017-04-29 10:39:49.091274','1','Standard Action Card',3,'',34,1),
	(434,'2017-04-29 10:40:03.366747','2','double grades permanent',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',34,1),
	(435,'2017-04-29 11:23:12.203270','4','double popularity next action',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',34,1),
	(436,'2017-04-29 11:24:28.846932','32','Distract Teacher (32): Generate 0 Trouble on your next action.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(437,'2017-04-29 11:27:18.645493','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(438,'2017-04-29 11:27:28.367491','4','double popularity next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(439,'2017-04-29 11:28:33.182104','33','Center of Attention (33): Double popularity on next action.',1,'[{\"added\": {}}]',19,1),
	(440,'2017-04-29 11:29:23.348186','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(441,'2017-04-29 12:01:15.310128','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(442,'2017-04-29 12:07:11.217957','4','double popularity next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(443,'2017-04-29 12:07:19.413969','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"expiry_criteria\"]}}]',34,1),
	(444,'2017-04-29 12:07:28.991626','33','Center of Attention (33): Double popularity on next action.',2,'[]',19,1),
	(445,'2017-04-29 19:02:45.015687','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(446,'2017-04-29 19:02:45.021199','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(447,'2017-04-29 19:02:45.027215','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(448,'2017-04-29 19:02:45.033701','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(449,'2017-04-29 19:02:45.040602','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(450,'2017-04-29 19:02:45.048694','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(451,'2017-04-29 19:02:45.057121','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(452,'2017-04-29 19:02:45.065181','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(453,'2017-04-29 19:02:45.074217','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(454,'2017-04-29 19:02:45.083763','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(455,'2017-04-29 19:02:45.092258','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(456,'2017-04-29 19:02:45.102150','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(457,'2017-04-29 19:02:45.111160','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(458,'2017-04-29 19:02:45.125176','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(459,'2017-04-29 19:02:45.133761','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(460,'2017-04-29 19:02:45.141967','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(461,'2017-04-29 19:02:45.149974','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(462,'2017-04-29 19:02:45.157811','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(463,'2017-04-29 19:02:45.165112','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(464,'2017-04-29 19:02:45.174212','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(465,'2017-04-29 19:02:45.182693','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(466,'2017-04-29 19:02:45.191694','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(467,'2017-04-29 19:02:45.200736','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(468,'2017-04-29 19:02:45.209759','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(469,'2017-04-29 19:02:45.218786','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(470,'2017-04-29 19:02:45.227808','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(471,'2017-04-29 19:24:26.907915','plus_one','plus_one',1,'[{\"added\": {}}]',32,1),
	(472,'2017-04-29 19:24:36.226003','5','+1 trouble/phase',1,'[{\"added\": {}}]',34,1),
	(473,'2017-04-29 19:24:39.621569','34','Fatigue (34): Ongoing: target Student +1 trouble/turn.',1,'[{\"added\": {}}]',19,1),
	(474,'2017-04-29 19:25:15.417263','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(475,'2017-04-29 19:25:15.423280','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(476,'2017-04-29 19:25:15.430590','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(477,'2017-04-29 19:25:15.436074','34','Fatigue (34): Ongoing: target Student +1 trouble/turn.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(478,'2017-04-29 19:25:46.473579','34','Fatigue (34): Ongoing: target Student +1 trouble/turn.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(479,'2017-04-29 19:26:18.406340','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(480,'2017-04-29 19:29:04.902202','6','+1 grades/phase',1,'[{\"added\": {}}]',34,1),
	(481,'2017-04-29 19:29:44.364640','35','School Supplies (35): Ongoing: +1 Grades per turn.',1,'[{\"added\": {}}]',19,1),
	(482,'2017-04-29 19:32:19.660592','7','popularity_0_for_phase',1,'[{\"added\": {}}]',34,1),
	(483,'2017-04-29 19:33:01.464349','36','Sick (36): Target student may not gain Popularity this round.',1,'[{\"added\": {}}]',19,1),
	(484,'2017-04-29 19:33:10.449349','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(485,'2017-04-29 19:33:10.455946','34','Fatigue (34): Ongoing: target Student +1 trouble/turn.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(486,'2017-04-29 19:33:10.462298','35','School Supplies (35): Ongoing: +1 Grades per turn.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(487,'2017-04-29 19:43:26.784979','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(488,'2017-04-29 19:43:26.791039','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(489,'2017-04-29 19:43:26.797424','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(490,'2017-04-29 19:44:27.054544','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(491,'2017-04-29 19:44:27.060559','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(492,'2017-04-29 19:44:27.071589','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(493,'2017-04-29 19:44:27.077632','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(494,'2017-04-29 20:38:21.595446','36','Sick (36): Target student may not gain Popularity this round.',2,'[]',19,1),
	(495,'2017-04-29 21:14:27.515762','37','Fall Asleep (37): Discard hand and redraw to full.',1,'[{\"added\": {}}]',19,1),
	(496,'2017-04-30 00:09:38.703196','31','Mutation Test (31): Mutation test',3,'',19,1),
	(497,'2017-04-30 00:09:56.312670','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(498,'2017-04-30 00:09:56.318839','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(499,'2017-04-30 00:09:56.325170','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(500,'2017-04-30 00:09:56.330981','33','Center of Attention (33): Double popularity on next action.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(501,'2017-04-30 00:09:56.341945','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(502,'2017-04-30 00:09:56.353670','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(503,'2017-04-30 00:09:56.361625','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(504,'2017-04-30 00:09:56.371088','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(505,'2017-04-30 00:09:56.381194','32','Distract Teacher (32): Generate 0 Trouble on your next action.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(506,'2017-04-30 00:09:56.390511','34','Fatigue (34): Ongoing: target Student +1 trouble/turn.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(507,'2017-04-30 00:09:56.399582','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(508,'2017-04-30 00:09:56.409197','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(509,'2017-04-30 00:09:56.417699','7','Pay Attention (7): +4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(510,'2017-04-30 00:09:56.427389','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(511,'2017-04-30 00:09:56.437032','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(512,'2017-04-30 00:09:56.446006','35','School Supplies (35): Ongoing: +1 Grades per turn.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(513,'2017-04-30 00:09:56.454195','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(514,'2017-04-30 00:09:56.462101','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(515,'2017-04-30 00:09:56.470213','15','Steal Test (15): +12 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(516,'2017-04-30 00:09:56.478313','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(517,'2017-04-30 00:09:56.492880','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(518,'2017-04-30 00:09:56.501833','19','Who Said That? (19): +3 Popularity. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(519,'2017-04-30 00:09:56.509983','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(520,'2017-04-30 01:34:32.395389','38','Test DIsmissal Card (38): I am a test!',1,'[{\"added\": {}}]',19,1),
	(521,'2017-04-30 01:37:05.677632','38','Test Discipline Card (38): I am a test!',2,'[{\"changed\": {\"fields\": [\"name\"]}}]',19,1),
	(522,'2017-04-30 02:08:44.289585','38','Test Discipline Card (38): I am a test!',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(523,'2017-04-30 02:09:15.087382','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"description\", \"name\"]}}]',19,1),
	(524,'2017-04-30 02:24:31.999314','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',1,'[{\"added\": {}}]',19,1),
	(525,'2017-04-30 02:26:48.179258','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',1,'[{\"added\": {}}]',19,1),
	(526,'2017-04-30 02:30:40.302926','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',1,'[{\"added\": {}}]',19,1),
	(527,'2017-04-30 02:33:22.647708','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',1,'[{\"added\": {}}]',19,1),
	(528,'2017-04-30 16:45:03.553550','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',1,'[{\"added\": {}}]',19,1),
	(529,'2017-04-30 16:55:03.758563','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(530,'2017-04-30 16:55:10.223953','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(531,'2017-04-30 16:55:10.231050','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(532,'2017-04-30 16:55:10.238704','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(533,'2017-04-30 16:55:10.245807','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(534,'2017-04-30 16:55:10.253265','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(535,'2017-04-30 16:56:04.999039','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(536,'2017-04-30 16:58:05.414741','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(537,'2017-04-30 16:59:29.138599','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(538,'2017-04-30 17:03:43.360295','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(539,'2017-04-30 17:04:34.527580','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(540,'2017-04-30 17:06:47.846448','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(541,'2017-04-30 17:09:23.620396','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(542,'2017-04-30 17:24:58.442393','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[]',19,1),
	(543,'2017-04-30 17:24:59.944016','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[]',19,1),
	(544,'2017-04-30 17:30:03.342744','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(545,'2017-04-30 17:30:03.349194','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(546,'2017-04-30 17:30:03.356001','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(547,'2017-04-30 17:30:03.363199','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(548,'2017-04-30 17:30:03.371170','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(549,'2017-04-30 17:49:37.716220','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(550,'2017-04-30 17:49:44.986951','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(551,'2017-04-30 17:50:24.543184','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(552,'2017-04-30 17:50:58.244280','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(553,'2017-04-30 17:51:28.499611','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(554,'2017-04-30 17:51:58.275229','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',2,'[{\"changed\": {\"fields\": [\"script\", \"active\"]}}]',19,1),
	(555,'2017-04-30 17:54:06.464558','8','double trouble from action card',1,'[{\"added\": {}}]',34,1),
	(556,'2017-04-30 17:54:09.384504','44','Troublemaker (44): Double trouble next round.\r\n1: +4 Popularity\r\n2-3: +2 Popularity',1,'[{\"added\": {}}]',19,1),
	(557,'2017-04-30 17:54:24.828096','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(558,'2017-04-30 17:54:24.835112','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(559,'2017-04-30 17:54:24.841630','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(560,'2017-04-30 17:54:24.848147','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(561,'2017-04-30 17:54:24.854665','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(562,'2017-04-30 17:54:24.861182','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(563,'2017-04-30 17:54:24.868201','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(564,'2017-04-30 17:54:24.874217','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(565,'2017-04-30 17:54:24.879732','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(566,'2017-05-04 10:41:12.433129','8','double trouble from action card',2,'[{\"changed\": {\"fields\": [\"gameflow_binding\"]}}]',34,1),
	(567,'2017-05-04 10:41:23.784423','7','popularity_0_for_phase',2,'[{\"changed\": {\"fields\": [\"gameflow_binding\"]}}]',34,1),
	(568,'2017-05-04 10:41:33.222006','6','+1 grades/phase',2,'[]',34,1),
	(569,'2017-05-04 10:41:38.831387','5','+1 trouble/phase',2,'[]',34,1),
	(570,'2017-05-04 10:41:48.097888','4','double popularity next action',2,'[{\"changed\": {\"fields\": [\"uses\"]}}]',34,1),
	(571,'2017-05-05 22:23:24.001583','44','Troublemaker (44): Double trouble next round.\r\n1: +4 Popularity\r\n2-3: +2 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(572,'2017-05-05 22:23:24.007097','5','Joke (5): +1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(573,'2017-05-05 22:29:50.839972','8','double trouble from action card',2,'[{\"changed\": {\"fields\": [\"gameflow_binding\"]}}]',34,1),
	(574,'2017-05-05 23:37:55.493386','8','double trouble from action card',2,'[{\"changed\": {\"fields\": [\"gameflow_binding\"]}}]',34,1),
	(575,'2017-05-05 23:38:06.118778','44','Troublemaker (44): Double trouble next classtime phase.\r\n1: +4 Popularity\r\n2-3: +2 Popularity',2,'[{\"changed\": {\"fields\": [\"description\"]}}]',19,1),
	(576,'2017-05-06 01:37:46.187657','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(577,'2017-05-06 01:37:46.195678','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(578,'2017-05-06 01:37:46.201193','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(579,'2017-05-06 01:37:46.206707','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(580,'2017-05-06 01:37:46.211721','33','Center of Attention (33): Double popularity on next action.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(581,'2017-05-06 01:37:46.218239','32','Distract Teacher (32): Generate 0 Trouble on your next action.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(582,'2017-05-06 01:37:46.223753','36','Sick (36): Target student may not gain Popularity this round.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(583,'2017-05-06 01:52:42.015451','3','0 trouble on next action',2,'[{\"changed\": {\"fields\": [\"uses\"]}}]',34,1),
	(584,'2017-05-13 15:05:42.830142','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(585,'2017-05-13 15:06:13.005063','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(586,'2017-05-13 15:06:26.140821','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(587,'2017-05-13 15:38:21.619746','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(588,'2017-05-13 15:39:58.521472','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(589,'2017-05-13 15:39:58.536510','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(590,'2017-05-13 15:39:58.543502','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(591,'2017-05-13 15:39:58.550521','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(592,'2017-05-13 15:39:58.557539','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(593,'2017-05-13 15:39:58.564558','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(594,'2017-05-13 15:39:58.571075','44','Troublemaker (44): Double trouble next classtime phase.\r\n1: +4 Popularity\r\n2-3: +2 Popularity',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(595,'2017-05-13 15:39:58.578625','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(596,'2017-05-13 15:39:58.586137','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(597,'2017-05-13 15:47:49.428694','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(598,'2017-05-13 15:49:03.342518','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(599,'2017-05-13 15:49:15.873405','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(600,'2017-05-13 15:50:00.222727','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(601,'2017-05-14 00:27:22.104933','20','A Better View (20): Move to an empty seat in a row further up. Grades +2 per row moved.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(602,'2017-05-14 00:27:49.510094','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(603,'2017-05-14 00:28:20.376238','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(604,'2017-05-14 00:28:53.126144','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(605,'2017-05-14 00:29:08.764849','33','Center of Attention (33): Double popularity on next action.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(606,'2017-05-14 00:29:32.735521','24','Cheat (24): Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(607,'2017-05-14 00:30:05.530328','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(608,'2017-05-14 00:30:23.147536','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(609,'2017-05-14 00:30:49.415263','6','Dean\'s List (6): +9 Popularity if you have the highest grades in the class.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(610,'2017-05-14 00:31:29.565464','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(611,'2017-05-14 00:31:53.051307','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(612,'2017-05-14 00:32:35.025394','29','Paper Airplane (29): Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(613,'2017-05-14 00:33:53.558498','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(614,'2017-05-14 00:34:04.717105','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(615,'2017-05-14 00:34:35.972330','27','Text (27): Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(616,'2017-05-14 00:35:00.211572','26','Uncontrollable (26): +3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(617,'2017-05-14 00:35:23.147360','25','Witty Comeback (25): Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(618,'2017-05-14 00:40:14.077739','19','Who Said That? (19): +3 Popularity, +2 Trouble. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"description\", \"trouble_cost\"]}}]',19,1),
	(619,'2017-05-14 00:41:28.351078','5','Joe Schmo',1,'[{\"added\": {}}]',18,1),
	(620,'2017-05-14 00:42:15.176287','6','Gene Kim',1,'[{\"added\": {}}]',18,1),
	(621,'2017-05-14 00:42:29.150056','7','Fredrick Vega',1,'[{\"added\": {}}]',18,1),
	(622,'2017-05-14 00:42:45.710589','8','Curtis Morrison',1,'[{\"added\": {}}]',18,1),
	(623,'2017-05-14 00:43:01.319104','9','Marta Castro',1,'[{\"added\": {}}]',18,1),
	(624,'2017-05-14 00:43:12.865919','10','Tommy Wolfe',1,'[{\"added\": {}}]',18,1),
	(625,'2017-05-14 00:43:26.753271','11','Catherine Alvarez',1,'[{\"added\": {}}]',18,1),
	(626,'2017-05-14 00:43:46.487559','12','Lorena Adams',1,'[{\"added\": {}}]',18,1),
	(627,'2017-05-14 00:44:03.691002','13','Mathilda Dowling',1,'[{\"added\": {}}]',18,1),
	(628,'2017-05-14 00:44:19.884504','14','Lelah Whelan',1,'[{\"added\": {}}]',18,1),
	(629,'2017-05-14 00:44:35.151561','15','Ha Crooks',1,'[{\"added\": {}}]',18,1),
	(630,'2017-05-14 00:45:02.827876','16','Rhea Macias',1,'[{\"added\": {}}]',18,1),
	(631,'2017-05-14 00:45:15.464057','17','Fredric Ponder',1,'[{\"added\": {}}]',18,1),
	(632,'2017-05-14 00:54:34.401306','4','double popularity next action',2,'[{\"changed\": {\"fields\": [\"tags\"]}}]',34,1),
	(633,'2017-05-14 01:29:24.866458','43','Relocation (43): Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(634,'2017-05-14 01:29:24.873619','21','Forgot to Shower (21): Each student to your immediate north, east, south, and west moves to an open seat of your choice.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(635,'2017-05-14 01:29:24.879994','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"active\"]}}]',19,1),
	(636,'2017-05-17 11:31:24.451707','28','Good Story (28): Move any two students to empty seats adjacent to you.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(637,'2017-05-18 21:41:25.572901','1','Argue with Teacher (1): +10 Popularity. -1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(638,'2017-05-18 21:41:43.896953','16','Ask Question (16): +6 Grades. -2 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(639,'2017-05-18 21:42:05.310195','12','Bully (12): Choose an adjacent student. That student receives -5 Popularity and a Torment token.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(640,'2017-05-18 21:42:23.889578','23','Console (23): Trouble -2. Remove torment from target student.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(641,'2017-05-18 21:42:47.441590','10','Cry (10): -2 Popularity. Remove a Torment token from yourself.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(642,'2017-05-18 21:43:09.736771','17','Group Project (17): All players +8 Grades. +4 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(643,'2017-05-18 21:43:28.201808','3','Pass Note (3): Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(644,'2017-05-18 21:43:46.623174','11','Principal\'s Office (11): Target actor +2 Trouble (regardless of row.)',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(645,'2017-05-18 21:44:00.664620','9','Pull Out Chair (9): Adjacent actor -6 Popularity.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(646,'2017-05-18 21:44:12.864117','22','Seat Reassignment (22): Swap any two student\'s seats or move a student to an empty seat.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(647,'2017-05-18 21:44:31.583365','18','Shush (18): +8 Grades. -1 Popularity per adjacent student.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(648,'2017-05-18 21:44:45.044813','13','Tattle Tale (13): -4 Popularity. -1 Trouble. Target actor +3 Trouble.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(649,'2017-05-18 21:44:58.387062','8','Tutor (8): +4 Popularity. +1 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(650,'2017-05-18 21:45:08.868605','14','Unprepared (14): Target actor -4 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(651,'2017-05-18 21:45:18.083775','19','Who Said That? (19): +3 Popularity, +2 Trouble. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(652,'2017-05-18 21:46:56.892935','39','Academic Reprimand (39): 1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(653,'2017-05-18 21:47:09.612704','40','Apology (40): 1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(654,'2017-05-18 21:47:29.938591','38','Mark on Perminent Record (38): -1 Grades, -1 Popularity per Trouble',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(655,'2017-05-18 21:47:52.777829','41','Public Scolding (41): 2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1),
	(656,'2017-05-18 21:48:21.036049','42','Suspension (42): All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',2,'[{\"changed\": {\"fields\": [\"script\"]}}]',19,1);

/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_content_type
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;

INSERT INTO `django_content_type` (`id`, `app_label`, `model`)
VALUES
	(37,'account','emailaddress'),
	(38,'account','emailconfirmation'),
	(1,'admin','logentry'),
	(2,'auth','group'),
	(4,'auth','permission'),
	(3,'auth','user'),
	(7,'authtoken','token'),
	(5,'contenttypes','contenttype'),
	(19,'game','card'),
	(9,'game','cardtype'),
	(30,'game','game'),
	(34,'game','mutationtemplate'),
	(32,'game','operationmodifier'),
	(35,'game','operationtag'),
	(31,'game','participant'),
	(18,'game','studentinfo'),
	(6,'sessions','session'),
	(36,'sites','site');

/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_migrations
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`)
VALUES
	(1,'contenttypes','0001_initial','2017-04-08 20:27:03.994710'),
	(2,'auth','0001_initial','2017-04-08 20:27:05.325487'),
	(3,'admin','0001_initial','2017-04-08 20:27:05.693595'),
	(4,'admin','0002_logentry_remove_auto_add','2017-04-08 20:27:05.709134'),
	(5,'contenttypes','0002_remove_content_type_name','2017-04-08 20:27:05.880906'),
	(6,'auth','0002_alter_permission_name_max_length','2017-04-08 20:27:06.013005'),
	(7,'auth','0003_alter_user_email_max_length','2017-04-08 20:27:06.163842'),
	(8,'auth','0004_alter_user_username_opts','2017-04-08 20:27:06.179169'),
	(9,'auth','0005_alter_user_last_login_null','2017-04-08 20:27:06.243388'),
	(10,'auth','0006_require_contenttypes_0002','2017-04-08 20:27:06.250299'),
	(11,'auth','0007_alter_validators_add_error_messages','2017-04-08 20:27:06.272683'),
	(12,'auth','0008_alter_user_username_max_length','2017-04-08 20:27:06.380548'),
	(13,'authtoken','0001_initial','2017-04-08 20:27:06.640374'),
	(14,'authtoken','0002_auto_20160226_1747','2017-04-08 20:27:06.807920'),
	(15,'game','0001_initial','2017-04-08 20:27:14.936848'),
	(16,'sessions','0001_initial','2017-04-08 20:27:15.034685'),
	(17,'game','0002_auto_20170408_1642','2017-04-08 20:42:56.731486'),
	(18,'game','0003_auto_20170408_1653','2017-04-08 20:53:11.074739'),
	(19,'game','0004_auto_20170408_1710','2017-04-08 21:10:56.893538'),
	(20,'game','0005_auto_20170408_1921','2017-04-08 23:22:01.093470'),
	(21,'game','0006_actor_trouble','2017-04-08 23:27:45.149785'),
	(22,'game','0007_actor_torment','2017-04-08 23:43:34.183771'),
	(23,'game','0008_auto_20170410_1933','2017-04-10 23:33:09.008727'),
	(24,'game','0009_remove_game_play_phase_count','2017-04-12 22:49:39.222687'),
	(25,'game','0010_auto_20170412_1929','2017-04-12 23:29:25.813141'),
	(26,'game','0011_card_description','2017-04-12 23:43:13.025058'),
	(27,'game','0012_auto_20170412_1945','2017-04-12 23:45:43.809721'),
	(28,'game','0013_auto_20170412_1946','2017-04-12 23:46:50.890639'),
	(29,'game','0014_card_trouble_cost','2017-04-13 00:01:29.516225'),
	(30,'game','0015_card_script','2017-04-14 23:06:10.934253'),
	(31,'game','0016_auto_20170414_1909','2017-04-14 23:09:42.070076'),
	(32,'game','0017_card_active','2017-04-14 23:16:39.428409'),
	(33,'game','0018_auto_20170414_1919','2017-04-14 23:19:05.087301'),
	(34,'game','0019_auto_20170414_1955','2017-04-14 23:55:57.939507'),
	(35,'game','0019_auto_20170415_0908','2017-04-15 13:09:01.112451'),
	(36,'game','0020_auto_20170415_0929','2017-04-15 13:29:56.845379'),
	(37,'game','0021_auto_20170415_0941','2017-04-15 13:41:03.983876'),
	(38,'game','0022_auto_20170415_1014','2017-04-15 14:14:55.163816'),
	(39,'game','0023_auto_20170415_1020','2017-04-15 14:20:58.524126'),
	(40,'game','0024_auto_20170417_2154','2017-04-18 01:54:33.544312'),
	(41,'game','0025_auto_20170422_1632','2017-04-22 20:32:39.701382'),
	(42,'game','0026_game_participant','2017-04-22 20:36:43.045638'),
	(43,'game','0002_mutationeffect','2017-04-27 00:21:04.503972'),
	(44,'game','0003_remove_mutationeffect_description','2017-04-27 00:26:09.319912'),
	(45,'game','0004_auto_20170426_2048','2017-04-27 00:48:45.046275'),
	(46,'game','0005_auto_20170427_1830','2017-04-27 22:30:31.146294'),
	(47,'game','0006_auto_20170427_1956','2017-04-27 23:56:49.265636'),
	(48,'game','0007_mutationtemplate_tags2','2017-04-28 21:51:37.054138'),
	(49,'game','0008_auto_20170428_1820','2017-04-28 22:20:20.191815'),
	(50,'game','0009_auto_20170428_1821','2017-04-28 22:21:07.506584'),
	(51,'game','0010_auto_20170428_1821','2017-04-28 22:21:51.295542'),
	(52,'game','0011_auto_20170428_1821','2017-04-28 22:21:51.571336'),
	(53,'game','0012_auto_20170428_1823','2017-04-28 22:23:58.182753'),
	(54,'game','0013_auto_20170428_1827','2017-04-28 22:27:12.911205'),
	(55,'game','0014_auto_20170428_1827','2017-04-28 22:27:28.596482'),
	(56,'game','0015_auto_20170428_1829','2017-04-28 22:29:13.076483'),
	(57,'game','0016_auto_20170428_1904','2017-04-28 23:04:50.014113'),
	(58,'game','0017_auto_20170428_1904','2017-04-29 01:22:54.849485'),
	(59,'game','0018_auto_20170428_2122','2017-04-29 01:22:54.879470'),
	(60,'game','0019_auto_20170428_2127','2017-04-29 01:27:57.127489'),
	(61,'game','0020_auto_20170429_0633','2017-04-29 10:33:21.472562'),
	(62,'game','0021_auto_20170429_0634','2017-04-29 10:34:06.276782'),
	(63,'game','0022_auto_20170429_0636','2017-04-29 10:36:37.229822'),
	(64,'game','0023_auto_20170429_0640','2017-04-29 10:40:58.913068'),
	(65,'game','0024_auto_20170429_0726','2017-04-29 11:26:41.783396'),
	(66,'game','0025_auto_20170429_1523','2017-04-29 19:23:16.986494'),
	(67,'game','0026_auto_20170429_1707','2017-04-29 21:07:14.618214'),
	(68,'game','0027_auto_20170504_0612','2017-05-04 10:12:34.839661'),
	(69,'game','0028_auto_20170505_0636','2017-05-05 10:36:16.987264'),
	(70,'game','0029_auto_20170505_1937','2017-05-05 23:37:44.887177'),
	(71,'game','0030_auto_20170507_0923','2017-05-07 13:23:51.065948'),
	(72,'account','0001_initial','2017-05-08 01:38:27.159026'),
	(73,'account','0002_email_max_length','2017-05-08 01:38:27.291925'),
	(74,'sites','0001_initial','2017-05-08 01:38:27.362182'),
	(75,'sites','0002_alter_domain_unique','2017-05-08 01:38:27.405979');

/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_session
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`)
VALUES
	('08fhmh1x4p9xfu1ca21w5jgq6z6peos1','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:53:56.394287'),
	('0nuzzkrq6abo9q4cne9pv343v6qw972g','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:17:43.253321'),
	('0pxexrhd2b26qi21ptoj5esodh6p7kjn','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:09:52.668092'),
	('10ojoxoyx2oqci5ftzcaz0r22n009l6c','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:49:22.594677'),
	('1w44chbrk3hejcl35hcbsx8bclr9zdud','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:34:12.888329'),
	('2f1rxmf8i0f7409fvay19ieujqx2eqf2','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-21 14:23:12.599122'),
	('2m72gvpsr3efkq37mwvfacx6tb71z6zr','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 22:13:30.530321'),
	('2nvqamj5fd3frwyk1exwmgpsjb3x7hc8','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:04:02.758766'),
	('2pkweo7l5t26sclm7sx51ns83646b8d2','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 22:31:20.477606'),
	('2vmnwsea47sdevhjme4s5jy8covjg5ot','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 21:16:17.419300'),
	('32jo3m025ypkpnib31m9ovoj7geh4e4v','N2VhNTkzYWQ2Zjc0NDBmZDNmOTA5NThmNjNmMzM4ZTg4OWZmMzdmMjp7Il9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MWYxOTQ5OGM0MDk0OTZkZmQ2NGM5NDFiMGM0MTEzOGQ3NWZhZDg4In0=','2017-05-25 00:46:23.619497'),
	('3h0qalvq0mobx1v1bcf7gjv673xhvnzt','NjgzMjlkOWUwZjIyZGYyYWQ1MmYzZDFmOTJhMzcwMzJlMGQ3OWEzMTp7Il9hdXRoX3VzZXJfaGFzaCI6IjkzMWQyMDAyZDdmNTZhMDY0N2VlMmJlNmU5NzZlZmM3ZWJkZGZkNTciLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiI2In0=','2017-05-22 01:53:46.574905'),
	('3ijpn64ah79t359143kqd3509e3w95xf','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:44:16.874821'),
	('47h99u9tujrkjfiw0thdsxoc4bwlpele','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:13:56.139628'),
	('47hytbftgcbg7c6f1ao9yv2m9e4vxnz3','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:22:57.376364'),
	('4gc3oy7cekb41eb84uzbqwnf1kiuf8x0','NzYyZGU1MjBkOTU3MjY5YTFlMGRlMjFmZTY2OWEwYWRhMWQyM2I3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlNjg0YWE3ZDFkM2Y5ZDVmNWEwMmM2NTFhNWMwZmE0MWFmMzRkNjQxIn0=','2017-06-01 12:35:44.028979'),
	('4hshnj1x6koifb94syrhtocnqaf1el49','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-25 00:45:36.923492'),
	('4ofg6gpqb85w3j91lyrkeu82j2471e52','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:06:47.681336'),
	('4rnkiei0n2kw4foa75yw8146kvy016j6','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 20:29:15.468080'),
	('4wtyi9yzjxnpxmvssq2mgiirgzfndow0','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:10:34.814920'),
	('52q50i5ydqt1gcykaiu2zrjw99b4qkti','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:01:14.423866'),
	('5hfcq4z9i0oa32sps83683iut833qe7k','Yjk2NTkwNWU0NTk5ZTJmMjM5MWM1ZjlkYjgxMzNmNWFkMTRiZDU2Nzp7Il9hdXRoX3VzZXJfaWQiOiI0IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJhY2NvdW50X3VzZXIiOiI0IiwiX2F1dGhfdXNlcl9oYXNoIjoiN2ViZTI3NDI3YTk1ZjM4ZDg1NzcyNDJlYWNhM2FlYzY5MGMyNDRhOCIsImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGx9','2017-05-22 01:45:56.701806'),
	('6tc02jozksp6iei0jso0pyh6wisg8aax','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:51:58.458939'),
	('7nspslzoh4fpd9f1yj8wcrda9f6zyk6v','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-21 14:47:11.017187'),
	('7w9rggu0lr3fk426wsma25amo8tuqpbn','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:58:59.173282'),
	('7x2clamycz0xnipm4jjkpypdkde3whyr','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:12:59.898775'),
	('87pnolng93pph0rm4jypqwjxw016k1qn','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:44:34.288454'),
	('8vvrtgyljtrov06dxnlvz5aew7xi5qc6','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:18:10.046722'),
	('93jxi1643nh33ixzl1rtkwyke53clwxl','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 22:31:13.410271'),
	('93mn2umognt5cenxld70qslwfklxs3rk','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-31 11:28:32.876512'),
	('99qst42bc3nmy8m4qh8nplk8b9frqwso','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:35:13.825619'),
	('a9npnl1f1daeb6sn0d8tgzeg4tld9lks','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-31 10:00:42.535700'),
	('bchsphzgwcxnnth7mkipg4c94i9ny15t','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-26 21:25:34.794044'),
	('biyljgs0g2rcsbsfnj5i8yapd388qkoh','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-21 14:50:14.747972'),
	('bjnvezn5kkq23k0t8vdapt9cnizrp0cl','OWY0NTU5ODVlNDI0NDBkNzM1NzA5ZDkwMmI0Nzk5NjIxNjFiN2Q4ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-28 15:51:18.610480'),
	('cfnzcmu57mj48s1hb84wrtox9q18km5x','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-21 14:47:09.807809'),
	('dih3pf61gbz5c2z6utrnvrykf0p3ug0c','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 21:07:05.025720'),
	('dwerkv6kujpt83y56327tg5ardp2j2cn','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:53:05.622087'),
	('el59f2kv72ddzty7elkgdk77rf3lejr9','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-26 21:47:54.795051'),
	('epk52hsvkjii2eo9a7pwbz4f03f8t50z','NGM1MWEwNjljNTVjYTg1NDY3ODQzYzFjNjY4ZTM5ODFiMTY4ZWY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-22 01:56:18.074760'),
	('f2hhu3u7ztewy2ld02gku1c79bqsb7qp','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:44:21.688177'),
	('fofi0xtdcpf46bafg88mxuxbdkvs634b','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:49:41.817852'),
	('fzwzscdsyfry6w2kmf6jkwgssa8ndhmu','M2NkMmQ1N2VkMjMyMDlmZDMwMjdhNmJkMTkyNTRlZTFkMjJhZjUzNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjY1NzE1OThjMTUzYWI5Y2Q2NzdiYzJlMjg0MzZjNmU4MDA1NzY0YWIiLCJfYXV0aF91c2VyX2lkIjoiOSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiYWNjb3VudF92ZXJpZmllZF9lbWFpbCI6bnVsbH0=','2017-05-26 21:36:00.702015'),
	('h3e3sztw0hcdd8u4ciajbngo2p12fb3t','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:20:16.395526'),
	('hl4hl2c2bmh20zwde0v6aiu0rrixnjvg','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-26 21:25:34.446321'),
	('hl7ptpkdun1v5hfgl0li9cnh9dmoixyh','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-26 21:47:57.240649'),
	('hsvd7uuh1wbajzhvt46xa75d8fsykz54','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:59:15.114616'),
	('hwvioiporaixdaeqgq7mz0e6djklti8e','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:04:11.929322'),
	('i9ntwte8w00ikkra1q1brojfpasb65m1','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:12:37.153988'),
	('iwpscautdd9bu7g1hdalsj6m682v174n','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 20:56:49.604380'),
	('j9sy7cvuvsc0dx20bfxwayec0as42sz8','MTk2YmY0ZDg0MWNmNmYxYzBkNTBjN2ZjYTllMDllNmJlN2E2NTI5Mzp7Il9hdXRoX3VzZXJfaGFzaCI6IjMwZTZiYzRiMmNiNmZjN2ZhN2I5OTc0MzMzZTY1NzdkMzRhNWVmN2QiLCJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJfYXV0aF91c2VyX2lkIjoiNyIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:54:41.589972'),
	('jbdt3x55h60ode1duabg10koj5jhoujz','OWY0NTU5ODVlNDI0NDBkNzM1NzA5ZDkwMmI0Nzk5NjIxNjFiN2Q4ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-22 01:58:00.760145'),
	('jdrp8or1uf0uq6z7p8drqgtuz9hmacqc','NGM1MWEwNjljNTVjYTg1NDY3ODQzYzFjNjY4ZTM5ODFiMTY4ZWY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-22 01:55:10.289357'),
	('jfywue1j1xnwt5q0uidykd89ax7m49oc','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:11:24.804690'),
	('jqmiwm6ayipgukpjcjdu5uzgixymwo0f','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:09:53.398546'),
	('k8u8p1ya3cla31v2noy26sxclw34xvst','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-28 11:39:33.683554'),
	('kaxf9iwgda3mq0poaci9nvlnf8n6x25b','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:06:03.671741'),
	('kfnw1er8x3qh8y48b5bxk9qnzjqg51wa','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:54:33.749580'),
	('klz5ykt4r4hkjz5c8v6ulsduj832z1fu','NTk3YTkyY2JmNmYzOTg4MTdmMzk1YzU1OTVjNjk1ODM2Yjg2YzIwNTp7Il9hdXRoX3VzZXJfaGFzaCI6IjkzMWQyMDAyZDdmNTZhMDY0N2VlMmJlNmU5NzZlZmM3ZWJkZGZkNTciLCJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJfYXV0aF91c2VyX2lkIjoiNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:53:35.590453'),
	('ll1htbrfq30a7icj0it77hj56tpgzzbu','OWViODYyYzVmNmYxMTQwMGY1NmU4N2UxYjdhZGY0MDgzYzNjNDZkNDp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2lkIjoiMSIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-26 21:45:22.424431'),
	('ln86fj2q92nokel7eqwoaqap6aep4muz','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:57:24.109800'),
	('lo2a9d0k4paslig6co0pl1wgnoim42wh','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 21:12:45.224697'),
	('lq6mf48a5qwfola5b0dbk4womk3ylkd2','YjU1ZTI5MjYzYjgwNGFjMDIwZDM3YTI1OGUwNDVlMDE0MTU4ZGVjZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YWMzZDc4ZmU5ZGU1NzIzNmIyMzBlNTFkMzRjMWM3OWRkYzcyNzkwIn0=','2017-04-27 00:11:58.254461'),
	('lzmjiqjuvecgsm7rbfr126ve2360jrx5','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:43:28.935578'),
	('m375b5ngt09brt26oq73c5me9gh4581q','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:03:44.416863'),
	('mb2jl22ij3nuj1smepdayoae535pc5me','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:38:39.033286'),
	('mcg13chvfrylp2omvktnthu4qbs25lzo','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-25 00:59:47.641555'),
	('mcwe2r1wpkhh47e1vhwom875tynv4s9t','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:05:39.564331'),
	('mx207lfqqlizinda4xyps3qd7909p2il','NGM1MWEwNjljNTVjYTg1NDY3ODQzYzFjNjY4ZTM5ODFiMTY4ZWY1NTp7Il9hdXRoX3VzZXJfaGFzaCI6ImVhZDM5YWU4YTdhMjdhZTRkODdiNTIyM2NhMjJkNzIwZDRkZTFkMDYiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-28 03:46:29.875494'),
	('oc64vji5h71zfynehkm8p0mr7f52lj9k','YjU1ZTI5MjYzYjgwNGFjMDIwZDM3YTI1OGUwNDVlMDE0MTU4ZGVjZTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1YWMzZDc4ZmU5ZGU1NzIzNmIyMzBlNTFkMzRjMWM3OWRkYzcyNzkwIn0=','2017-04-27 00:13:22.760568'),
	('oce90qn0tutoa249ytfw9zpugcquy1td','NjM0Yjc1MmM1OTNmZjMzM2IxYTk3Yjg2OTk1YjAyMDJlMjYxN2IxNzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiJlYWQzOWFlOGE3YTI3YWU0ZDg3YjUyMjNjYTIyZDcyMGQ0ZGUxZDA2In0=','2017-05-25 00:46:26.861061'),
	('p2lxzrq01bs1jxewuq3atxef1fyerjyh','OWY0NTU5ODVlNDI0NDBkNzM1NzA5ZDkwMmI0Nzk5NjIxNjFiN2Q4ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-28 16:12:48.569286'),
	('p5bevy430ji9ohxbnj5ctml8snywm1ga','M2NkN2YyYzAyNDY1NTllZDI1MGMzODAyYWFjZTZiN2RiNWE3NDM3NTp7Il9hdXRoX3VzZXJfaWQiOiI1IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJhY2NvdW50X3ZlcmlmaWVkX2VtYWlsIjpudWxsLCJfYXV0aF91c2VyX2hhc2giOiIyNjhmMzBmNjc3NmM1ZmFiZDZkYWM3MzBiYmRhMDAyNDUwZDEzOWFhIiwiYWNjb3VudF91c2VyIjoiNSJ9','2017-05-22 01:51:53.244757'),
	('plauwnvahaqqdppbxqnhottlkslsza0n','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:15:45.736401'),
	('q8fuj74oou9w4b5a1utezbw7whc7gglg','OWY0NTU5ODVlNDI0NDBkNzM1NzA5ZDkwMmI0Nzk5NjIxNjFiN2Q4ZDp7Il9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-05-27 22:40:40.783663'),
	('qaf5p563ortr31qksk89ll8le67vk9ff','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:25:46.662358'),
	('r6nxy7vcj74vwl5lak31uvnbcvu8j6rq','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:00:13.988020'),
	('rhqkbpm85ysutwmyjpu65dvjvo3mzaxq','YmM5Njk2OWZmODVlOGExNGM0M2I5MDhhYzQxNWNhZGQxNWMxY2I1NDp7ImFjY291bnRfdmVyaWZpZWRfZW1haWwiOm51bGwsIl9hdXRoX3VzZXJfaWQiOiI4IiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI4MWYxOTQ5OGM0MDk0OTZkZmQ2NGM5NDFiMGM0MTEzOGQ3NWZhZDg4In0=','2017-05-25 00:46:15.320757'),
	('rqgx0n8k7j83xk0jhb17h37u31vrxxu6','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:16:53.147131'),
	('rwrz1bdz0abo4pykrpo0kaqmw2ml1q0f','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:59:12.335930'),
	('so6ig0op47xztkit37f1hqvxtocmm8vq','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:09:46.192606'),
	('td1k1lo3cqohvwi382hz9rs43stbvhij','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:47:00.823598'),
	('truhwvl3k52762v0nd5mikdykmzkjo63','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:54:56.712513'),
	('umlc2o2s0pkr5i4r9pltreovwwz33xop','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:49:57.267171'),
	('uoqdgq5myjdvjm8m8trl3kvc2ecmvagf','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:23:47.773575'),
	('vdo79v9r5gpd5qr58ojmn7x1o4tzusyr','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:15:07.566311'),
	('vm6fpbi24kp2ag976ei1awgd5nfcppri','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:47:04.064047'),
	('vrk0sgtuo4aev6t032yck1rbf0yjmb22','MmYyMzdkNDFjODFkZGYwYTFmMWI4ZTgyNTU4MjM1MjdjMmYzN2JlMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNWFjM2Q3OGZlOWRlNTcyMzZiMjMwZTUxZDM0YzFjNzlkZGM3Mjc5MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-04-22 20:27:52.165754'),
	('wu7zjmoqdr1ze77v1xlp7a38ykzmm9y9','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:13:33.609810'),
	('xn8v5dsfjqaio9ftt31z8x4o6j6o89e0','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 00:55:00.894110'),
	('xw2z0aslxu3vqhhc4ny4biandtnpcv9b','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:14:28.274532'),
	('yl3bpcwshigpjw6r539q22nri0xlg15q','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 17:14:39.426102'),
	('ysz78zymony21s5pbbdde56qitctqqq1','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-22 01:19:27.342812'),
	('yvg96efxiiigtkmbjkyfgouu7pa4i5ih','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 18:43:19.355963'),
	('z31hemql9qhmokexjez84tstfh57fi98','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-21 19:24:14.778309'),
	('z52wre6yj4iubziffef9nnop5sq9xx99','MzdhMDY3YmU1ZGE5NGMxMjllZjA1MjEwMDA2OTcyYWVmODc3MWYwMTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiZWFkMzlhZThhN2EyN2FlNGQ4N2I1MjIzY2EyMmQ3MjBkNGRlMWQwNiIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=','2017-05-30 10:31:43.191161');

/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table django_site
# ------------------------------------------------------------

DROP TABLE IF EXISTS `django_site`;

CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_site_domain_a2e37b91_uniq` (`domain`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;

INSERT INTO `django_site` (`id`, `domain`, `name`)
VALUES
	(1,'example.com','example.com');

/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_card
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_card`;

CREATE TABLE `game_card` (
  `created` datetime(6) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `card_type_id` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `trouble_cost` int(11) NOT NULL,
  `script` longtext NOT NULL,
  `active` tinyint(1) NOT NULL,
  `mutation_template_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `game_card_name_af222744_uniq` (`name`),
  KEY `game_card_card_type_id_81d05bd7_fk_game_cardtype_id` (`card_type_id`),
  KEY `game_c_mutation_template_id_c66624c0_fk_game_mutationtemplate_id` (`mutation_template_id`),
  CONSTRAINT `game_c_mutation_template_id_c66624c0_fk_game_mutationtemplate_id` FOREIGN KEY (`mutation_template_id`) REFERENCES `game_mutationtemplate` (`id`),
  CONSTRAINT `game_card_card_type_id_81d05bd7_fk_game_cardtype_id` FOREIGN KEY (`card_type_id`) REFERENCES `game_cardtype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_card` WRITE;
/*!40000 ALTER TABLE `game_card` DISABLE KEYS */;

INSERT INTO `game_card` (`created`, `id`, `name`, `card_type_id`, `description`, `trouble_cost`, `script`, `active`, `mutation_template_id`)
VALUES
	('2017-04-08 20:32:11.000000',1,'Argue with Teacher','Action Card','+10 Popularity. -1 Grades.',4,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.subtract_grades(requestor, 1)\r\nActorApi.add_popularity(requestor, 10)',1,NULL),
	('2017-04-08 21:03:56.000000',3,'Pass Note','Action Card','Pass a note to any student in your row or column. +3 Popularity per student that sees the note.',3,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nseats = SeatApi.get_filled_seats()\r\nr_seat = requestor.student.seat\r\n\r\neligible_seats = []\r\nfor s in seats:\r\n    if s.id != r_seat.id and (s.row == r_seat.row or s.column == r_seat.column) and s.student is not None:\r\n        eligible_seats.append(s)\r\neligible_students = [s.student for s in eligible_seats]\r\n\r\nselected_student = PromptApi.prompt_student_choice(eligible_students, \"Target Student\")\r\n\r\ns_seat = selected_student.seat\r\nfield = \"column\" if s_seat.column != r_seat.column else \"row\"\r\n\r\nr_seat_dim = getattr(r_seat, field)\r\ns_seat_dim = getattr(s_seat, field)\r\nmax_dim = max(r_seat_dim, s_seat_dim)\r\nmin_dim = min(r_seat_dim, s_seat_dim)\r\nin_between = lambda s: getattr(s, field) <= max_dim and getattr(s, field) >= min_dim\r\n\r\neligible_seats = filter(lambda s: s.id != r_seat.id, seats)\r\nmatching_seats = filter(in_between, eligible_seats)\r\nvalue = 3 * len(list(matching_seats))\r\n\r\nActorApi.add_popularity(requestor, value)',1,NULL),
	('2017-04-08 21:32:14.000000',5,'Joke','Action Card','+1 Popularity per adjacent student.',3,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nadjacent_students = StudentApi.get_adjacent_students(requestor.student)\r\nadjacent_students_count = len(adjacent_students)\r\nActorApi.add_popularity(requestor, adjacent_students_count)',1,NULL),
	('2017-04-08 22:51:23.000000',6,'Dean\'s List','Action Card','+9 Popularity if you have the highest grades in the class.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nother_students = ActorApi.get_all_but_requestor()\r\nif requestor.grades > max([s.grades for s in other_students]):\r\n    ActorApi.add_popularity(requestor, 9)',1,NULL),
	('2017-04-08 23:13:20.000000',7,'Pay Attention','Action Card','+4 Grades.',0,'requestor = ActorApi.get_requestor()\r\nActorApi.add_grades(requestor, 4)',1,NULL),
	('2017-04-08 23:14:36.000000',8,'Tutor','Action Card','+4 Popularity. +1 Grades.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_popularity(requestor, 4)\r\nActorApi.add_grades(requestor, 1)',1,NULL),
	('2017-04-08 23:19:38.000000',9,'Pull Out Chair','Action Card','Adjacent actor -6 Popularity.',2,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_actors = ActorApi.get_adjacent_actors(requestor)\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\nActorApi.subtract_popularity(selected_actor, 6)',1,NULL),
	('2017-04-08 23:47:02.000000',10,'Cry','Action Card','-2 Popularity. Remove a Torment token from yourself.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.subtract_torment(requestor, 1)\r\nActorApi.subtract_popularity(requestor, 2)',1,NULL),
	('2017-04-08 23:48:20.000000',11,'Principal\'s Office','Action Card','Target actor +2 Trouble (regardless of row.)',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\neligible_actors = ActorApi.get_actors()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\nActorApi.add_trouble(selected_actor, 2)',1,NULL),
	('2017-04-10 23:25:36.000000',12,'Bully','Action Card','Choose an adjacent student. That student receives -5 Popularity and a Torment token.',5,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_students = StudentApi.get_adjacent_students(requestor.student)\r\nselected_student = PromptApi.prompt_student_choice(eligible_students, \"Target Student\")\r\nif selected_student.controlled:\r\n    ActorApi.subtract_popularity(selected_student.actor, 5)\r\n    ActorApi.add_torment(selected_student.actor, 1)',1,NULL),
	('2017-04-10 23:27:03.000000',13,'Tattle Tale','Action Card','-4 Popularity. -1 Trouble. Target actor +3 Trouble.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_actors = ActorApi.get_all_but_requestor()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\nActorApi.add_trouble(selected_actor, 3)\r\nActorApi.subtract_popularity(requestor, 4)\r\nActorApi.subtract_trouble(requestor, 1)',1,NULL),
	('2017-04-10 23:30:03.000000',14,'Unprepared','Action Card','Target actor -4 Grades.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\neligible_actors = ActorApi.get_all_but_requestor()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\nActorApi.subtract_grades(selected_actor, 4)',1,NULL),
	('2017-04-10 23:31:40.000000',15,'Steal Test','Action Card','+12 Grades.',5,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_grades(requestor, 12)',1,NULL),
	('2017-04-10 23:33:13.000000',16,'Ask Question','Action Card','+6 Grades. -2 Popularity.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_grades(requestor, 6)\r\nActorApi.subtract_popularity(requestor, 2)',1,NULL),
	('2017-04-10 23:36:21.000000',17,'Group Project','Action Card','All players +8 Grades. +4 Popularity.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nall_actors = ActorApi.get_actors()\r\nfor actor in all_actors:\r\n    ActorApi.add_grades(actor, 8)\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_popularity(requestor, 4)',1,NULL),
	('2017-04-10 23:37:33.000000',18,'Shush','Action Card','+8 Grades. -1 Popularity per adjacent student.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_grades(requestor, 8)\r\nadjacent_students_count = len(StudentApi.get_adjacent_students(requestor.student))\r\nActorApi.add_popularity(requestor, -adjacent_students_count)',1,NULL),
	('2017-04-10 23:39:50.000000',19,'Who Said That?','Action Card','+3 Popularity, +2 Trouble. Set all players\' trouble equal to yours (after applying the trouble this card generates.)',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_popularity(requestor, 3)\r\nActorApi.add_trouble(requestor, 2)\r\nother_actors = ActorApi.get_all_but_requestor()\r\nfor actor in other_actors:\r\n    ActorApi.set_trouble(actor, requestor.trouble)',1,NULL),
	('2017-04-15 02:23:51.000000',20,'A Better View','Action Card','Move to an empty seat in a row further up. Grades +2 per row moved.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nempty_seats = SeatApi.get_empty_seats()\r\nrequestor_row = requestor.student.seat.row\r\nempty_seats_ahead_of_requestor = list(filter(lambda s: s.row < requestor_row, empty_seats))\r\n\r\nselected_seat = PromptApi.prompt_seat_choice(empty_seats_ahead_of_requestor, \"Target Seat\")\r\n\r\nrow_diff = requestor_row - selected_seat.row\r\nStudentApi.move_to_empty_seat(requestor.student, selected_seat)\r\nActorApi.add_grades(requestor, 2 * row_diff)',1,NULL),
	('2017-04-15 02:34:42.000000',21,'Forgot to Shower','Action Card','Each student to your immediate north, east, south, and west moves to an open seat of your choice.',1,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nimmediate_students = StudentApi.get_immediate_students(requestor.student)\r\nempty_seats = SeatApi.get_empty_seats()\r\n\r\nstudent_seat_actions = []\r\nfor student in immediate_students:\r\n    selected_seat = PromptApi.prompt_seat_choice(empty_seats, \"Target Seat for Student {} ({})\".format(student.name, student.id))\r\n    student_seat_actions.append((student, selected_seat))\r\n    empty_seats.remove(selected_seat)\r\n\r\nfor student, seat in student_seat_actions:\r\n    StudentApi.move_to_empty_seat(student, seat)',1,NULL),
	('2017-04-15 02:42:36.000000',22,'Seat Reassignment','Action Card','Swap any two student\'s seats or move a student to an empty seat.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nall_seats = SeatApi.get_seats()\r\nall_students = StudentApi.get_students()\r\nselected_student = PromptApi.prompt_student_choice(all_students, \"Target Student\")\r\n\r\neligible_seats = list(filter(lambda s: s.id != selected_student.seat.id, all_seats))\r\nselected_seat = PromptApi.prompt_seat_choice(eligible_seats, \"Target Seat for {} ({})\".format(selected_student.name, selected_student.id))\r\n\r\nif selected_seat.empty:\r\n    StudentApi.move_to_empty_seat(selected_student, selected_seat)\r\nelse:\r\n    StudentApi.swap_seat(selected_student, selected_seat)',1,NULL),
	('2017-04-15 11:31:22.000000',23,'Console','Action Card','Trouble -2. Remove torment from target student.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_students = StudentApi.get_adjacent_students(requestor.student)\r\nselected_student = PromptApi.prompt_student_choice(eligible_students, \"Target Student\")\r\nif selected_student.controlled:\r\n    ActorApi.subtract_torment(selected_student.actor, 1)\r\nActorApi.subtract_trouble(requestor, 2)',1,NULL),
	('2017-04-15 11:33:11.000000',24,'Cheat','Action Card','Gain an amount of Trouble from 1 to 5. Gain double that in Grades.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\ntrouble_amount = PromptApi.prompt_number_choice(list(range(1, 6)), \"Trouble Amount\")\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_trouble(requestor, trouble_amount)\r\nActorApi.add_grades(requestor, 2 * trouble_amount)',1,NULL),
	('2017-04-15 11:41:48.000000',25,'Witty Comeback','Action Card','Remove a Torment token on yourself to gain 5 Popularity. (You must have a torment token.)',1,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nif requestor.torment > 0:\r\n    ActorApi.add_torment(requestor, -1)\r\n    ActorApi.add_popularity(requestor, 5)',1,NULL),
	('2017-04-15 11:43:19.000000',26,'Uncontrollable','Action Card','+3 Popularity per Trouble token on yourself. (You gain the trouble from this card after the effect takes place.)',2,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.add_popularity(requestor, 3 * requestor.trouble)',1,NULL),
	('2017-04-15 11:45:10.000000',27,'Text','Action Card','Choose a player. Gain 10 Popularity if they are more popular than you, otherwise 5. If they are in the front row, they gain 1 Trouble.',2,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_actors = ActorApi.get_all_but_requestor()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\nif selected_actor.popularity > requestor.popularity:\r\n    ActorApi.add_popularity(requestor, 10)\r\nelse:\r\n    ActorApi.add_popularity(requestor, 5)\r\n\r\nif selected_actor.student.seat.row == 0:\r\n    ActorApi.add_trouble(selected_actor, 1)',1,NULL),
	('2017-04-15 11:54:36.000000',28,'Good Story','Action Card','Move any two students to empty seats adjacent to you.',2,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_students = StudentApi.get_all_but_requestor()\r\nadjacent_seats = SeatApi.get_adjacent_seats(requestor.student.seat)\r\nempty_seats = [s for s in adjacent_seats if s.empty]\r\n\r\nif len(empty_seats) > 0:\r\n    selected_student1 = PromptApi.prompt_student_choice(eligible_students, \"Target Student 1\")\r\n    selected_seat1 = PromptApi.prompt_seat_choice(empty_seats, \"Target Student 1 Seat\")\r\n    empty_seats = [s for s in empty_seats if s is not selected_seat1]\r\n    if len(empty_seats) > 0:\r\n        selected_student2 = PromptApi.prompt_student_choice(eligible_students, \"Target Student 2\")\r\n        selected_seat2 = PromptApi.prompt_seat_choice(empty_seats, \"Target Student 2 Seat\")\r\n        StudentApi.move_to_empty_seat(selected_student2, selected_seat2)\r\n    StudentApi.move_to_empty_seat(selected_student1, selected_seat1)',1,NULL),
	('2017-04-15 12:01:16.000000',29,'Paper Airplane','Action Card','Throw a paper airplane to the front of class. Popularity +3 for each row it goes through.',3,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nrequestor_row = requestor.student.seat.row\r\nActorApi.add_popularity(requestor, 3 * requestor_row)',1,NULL),
	('2017-04-29 00:56:36.000000',32,'Distract Teacher','Action Card','Generate 0 Trouble on your next action.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nexport(\"targeted_actor_id\", requestor.id)',1,3),
	('2017-04-29 11:26:49.000000',33,'Center of Attention','Action Card','Double popularity on next action.',1,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\n\r\nrequestor = ActorApi.get_requestor()\r\nexport(\"targeted_actor_id\", requestor.id)',1,4),
	('2017-04-29 19:19:38.000000',34,'Fatigue','Action Card','Ongoing: target Student +1 trouble/turn.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_actors = ActorApi.get_actors()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\n\r\nexport(\"targeted_actor_id\", selected_actor.id)',1,5),
	('2017-04-29 19:28:05.000000',35,'School Supplies','Action Card','Ongoing: +1 Grades per turn.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nexport(\"targeted_actor_id\", requestor.id)',1,6),
	('2017-04-29 19:30:46.000000',36,'Sick','Action Card','Target student may not gain Popularity this round.',0,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\neligible_actors = ActorApi.get_actors()\r\nselected_actor = PromptApi.prompt_actor_choice(eligible_actors, \"Target Actor\")\r\n\r\nexport(\"targeted_actor_id\", selected_actor.id)',1,7),
	('2017-04-29 20:40:41.000000',37,'Fall Asleep','Action Card','Discard hand and redraw to full.',2,'# +- ACTION CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END ACTION CARD BOILERPLATE -------+\r\n\r\nrequestor = ActorApi.get_requestor()\r\nActorApi.refresh_hand(requestor)',1,NULL),
	('2017-04-30 01:34:12.000000',38,'Mark on Perminent Record','Discipline Card','-1 Grades, -1 Popularity per Trouble',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nactor = ActorApi.get_requestor()\r\ntrouble = actor.trouble\r\nActorApi.subtract_grades(actor, trouble)\r\nActorApi.subtract_popularity(actor, trouble)',1,NULL),
	('2017-04-30 02:21:30.000000',39,'Academic Reprimand','Discipline Card','1 Trouble: -1 Grades\r\n2 Trouble: -2 Grades\r\n3 Trouble: -4 Grades\r\n4+ Trouble: -6 Grades',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\npenalties = {\r\n    1: 1,\r\n    2: 2,\r\n    3: 4,\r\n    4: 5\r\n}\r\nactor = ActorApi.get_requestor()\r\ntrouble = min(actor.trouble, 4)\r\nif trouble > 0:\r\n    ActorApi.subtract_grades(actor, penalties[trouble])',1,NULL),
	('2017-04-30 02:25:13.000000',40,'Apology','Discipline Card','1 Trouble: -2 Popularity\r\n2 Trouble: -4 Popularity\r\n3 Trouble: -6 Popularity\r\n4 Trouble: -8 Popularity\r\n5+ Trouble: -10 Popularity',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nactor = ActorApi.get_requestor()\r\ntrouble = min(actor.trouble, 5)\r\nif trouble > 0:\r\n    ActorApi.subtract_popularity(actor, 2 * trouble)',1,NULL),
	('2017-04-30 02:28:12.000000',41,'Public Scolding','Discipline Card','2-3 Trouble : +1 Torment\r\n4 Trouble: +1 Torment, -3 Popularity\r\n5+ Trouble: +1 Torment, -6 Popularity',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nactor = ActorApi.get_requestor()\r\ntrouble = min(actor.trouble, 5)\r\nif trouble >= 2:\r\n    ActorApi.add_torment(actor, 1)\r\n    if trouble == 4:\r\n        ActorApi.subtract_popularity(actor, 3)\r\n    elif trouble > 4:\r\n        ActorApi.subtract_popularity(actor, 6)',1,NULL),
	('2017-04-30 02:31:29.000000',42,'Suspension','Discipline Card','All students with no Trouble +4 Grades.\r\nAll students with 3+ Trouble -2 Grades.',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nactor = ActorApi.get_requestor()\r\ntrouble = actor.trouble\r\nif trouble == 0:\r\n    ActorApi.add_grades(actor, 4)\r\nelif trouble > 3:\r\n    ActorApi.subtract_grades(actor, 2)',1,NULL),
	('2017-04-30 16:43:57.000000',43,'Relocation','Discipline Card','Lowest popularity student chooses your new seat.\r\n1: same row\r\n2: same column\r\n3+: anywhere',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nsorted_by_popularity = list(sorted(ActorApi.get_actors(), key=lambda x: x.popularity))\r\nlowest_popularity = sorted_by_popularity[0]\r\nif lowest_popularity.id == ActorApi.get_requestor().id:\r\n    empty_seats = SeatApi.get_empty_seats()\r\n    results = {}\r\n\r\n    for actor in sorted_by_popularity:\r\n        student = actor.student\r\n        eligible_seats = []\r\n        if actor.trouble <= 0:\r\n            continue\r\n        elif actor.trouble == 1:\r\n            eligible_seats = filter(lambda s: s.row == student.seat.row, empty_seats)\r\n        elif actor.trouble == 2:\r\n            eligible_seats = filter(lambda s: s.column == student.seat.column, empty_seats)\r\n        elif actor.trouble >= 3:\r\n            eligible_seats = empty_seats\r\n        eligible_seats = list(filter(lambda s: s.id not in results.keys(), eligible_seats))\r\n        if eligible_seats:\r\n            selected_seat = PromptApi.prompt_seat_choice(eligible_seats, \"Target Seat for Student {} ({})\".format(student.name, student.id))\r\n            results[selected_seat] = actor.student\r\n\r\n    for student, seat in results.items():\r\n        StudentApi.move_to_empty_seat(seat, student)',1,NULL),
	('2017-04-30 17:52:04.000000',44,'Troublemaker','Discipline Card','Double trouble next classtime phase.\r\n1: +4 Popularity\r\n2-3: +2 Popularity',0,'# +- DISCIPLINE CARD BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\nPromptApi = __locals.get(\'PromptApi\')\r\nexport = __locals.get(\'export\')\r\n# +- END DISCIPLINE CARD BOILERPLATE -------+\r\n\r\nactor = ActorApi.get_requestor()\r\n\r\nif actor.trouble == 1:\r\n    ActorApi.add_popularity(actor, 4)\r\nelif actor.trouble in (2, 3):\r\n    ActorApi.add_popularity(actor, 2)\r\n\r\nexport(\"targeted_actor_id\", actor.id)',1,8);

/*!40000 ALTER TABLE `game_card` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_cardtype
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_cardtype`;

CREATE TABLE `game_cardtype` (
  `created` datetime(6) NOT NULL,
  `id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_cardtype` WRITE;
/*!40000 ALTER TABLE `game_cardtype` DISABLE KEYS */;

INSERT INTO `game_cardtype` (`created`, `id`)
VALUES
	('2017-04-29 21:53:34.000000','Action Card'),
	('2017-04-29 21:53:41.000000','After School Card'),
	('2017-04-29 21:53:50.000000','Discipline Card');

/*!40000 ALTER TABLE `game_cardtype` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_game
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_game`;

CREATE TABLE `game_game` (
  `created` datetime(6) NOT NULL,
  `id` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table game_mutationtemplate
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_mutationtemplate`;

CREATE TABLE `game_mutationtemplate` (
  `created` datetime(6) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `priority` int(11) NOT NULL,
  `match_all` tinyint(1) NOT NULL,
  `operation_modifier_id` varchar(255) NOT NULL,
  `tags` varchar(381) NOT NULL,
  `name` varchar(255) NOT NULL,
  `gameflow_binding` varchar(255) NOT NULL,
  `uses` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `game_operation_modifier_id_31260955_fk_game_operationmodifier_id` (`operation_modifier_id`),
  CONSTRAINT `game_operation_modifier_id_31260955_fk_game_operationmodifier_id` FOREIGN KEY (`operation_modifier_id`) REFERENCES `game_operationmodifier` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_mutationtemplate` WRITE;
/*!40000 ALTER TABLE `game_mutationtemplate` DISABLE KEYS */;

INSERT INTO `game_mutationtemplate` (`created`, `id`, `priority`, `match_all`, `operation_modifier_id`, `tags`, `name`, `gameflow_binding`, `uses`)
VALUES
	('2017-04-28 23:01:48.000000',2,0,0,'double','Grades,Permanent','double grades permanent','Game',NULL),
	('2017-04-29 01:03:40.000000',3,0,1,'floor_0','Action Card Cost,Card Cost,Trouble','0 trouble on next action','Game',1),
	('2017-04-29 09:58:53.000000',4,0,1,'double','Card,Popularity,Actor Action,Played Card,Action Card','double popularity next action','Game',1),
	('2017-04-29 19:23:19.000000',5,0,0,'plus_one','Trouble per Turn','+1 trouble/phase','Game',NULL),
	('2017-04-29 19:28:30.000000',6,0,0,'plus_one','Grades per Turn','+1 grades/phase','Game',NULL),
	('2017-04-29 19:31:07.000000',7,99,0,'floor_0','Popularity','popularity_0_for_phase','Phase',NULL),
	('2017-04-30 17:53:01.000000',8,0,0,'double','Trouble,Action Card Cost','double trouble from action card','Next Classtime Phase',NULL);

/*!40000 ALTER TABLE `game_mutationtemplate` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_operationmodifier
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_operationmodifier`;

CREATE TABLE `game_operationmodifier` (
  `created` datetime(6) NOT NULL,
  `id` varchar(255) NOT NULL,
  `script` longtext NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_operationmodifier` WRITE;
/*!40000 ALTER TABLE `game_operationmodifier` DISABLE KEYS */;

INSERT INTO `game_operationmodifier` (`created`, `id`, `script`, `active`)
VALUES
	('2017-04-27 00:26:56.000000','double','# +- BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\noperation = __locals.get(\'operation\')\r\nexport = __locals.get(\'export\')\r\n# +- END BOILERPLATE -------+\r\n\r\noperation.value *= 2\r\nexport(\"operation\", operation)',1),
	('2017-04-29 01:05:03.000000','floor_0','# +- OPERATION_MODIFIER BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\noperation = __locals.get(\'operation\')\r\nexport = __locals.get(\'export\')\r\n# +- END OPERATION_MODIFIER BOILERPLATE -------+\r\n\r\noperation.value = 0\r\nexport(\"operation\", operation)',1),
	('2017-04-29 19:23:38.000000','plus_one','# +- OPERATION_MODIFIER BOILERPLATE -------+\r\n__locals = locals()\r\nActorApi = __locals.get(\'ActorApi\')\r\nStudentApi = __locals.get(\'StudentApi\')\r\nSeatApi = __locals.get(\'SeatApi\')\r\noperation = __locals.get(\'operation\')\r\nexport = __locals.get(\'export\')\r\n# +- END OPERATION_MODIFIER BOILERPLATE -------+\r\n\r\noperation.value += 1\r\nexport(\"operation\", operation)',1);

/*!40000 ALTER TABLE `game_operationmodifier` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_operationtag
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_operationtag`;

CREATE TABLE `game_operationtag` (
  `created` datetime(6) NOT NULL,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_operationtag` WRITE;
/*!40000 ALTER TABLE `game_operationtag` DISABLE KEYS */;

INSERT INTO `game_operationtag` (`created`, `name`)
VALUES
	('2017-04-28 20:30:42.000000','ActionCard'),
	('2017-04-28 20:29:29.000000','ActorAction'),
	('2017-04-28 20:30:33.000000','AfterSchoolCard'),
	('2017-04-28 20:31:09.000000','AfterSchoolCardCost'),
	('2017-04-28 20:30:56.000000','AutomaticCard'),
	('2017-04-28 20:29:49.000000','AutomaticEffect'),
	('2017-04-28 20:29:58.000000','Card'),
	('2017-04-28 20:31:19.000000','CardCost'),
	('2017-04-28 20:30:25.000000','DisciplineCard'),
	('2017-04-28 20:34:21.000000','Grades'),
	('2017-04-28 20:31:34.000000','OnDraw'),
	('2017-04-28 20:32:56.000000','Permanent'),
	('2017-04-28 20:31:49.000000','PhaseBound'),
	('2017-04-28 20:30:50.000000','PlayedCard'),
	('2017-04-28 20:34:10.000000','Popularity'),
	('2017-04-28 20:31:25.000000','ProximateEffect'),
	('2017-04-28 20:31:57.000000','StageBound'),
	('2017-04-28 20:29:41.000000','StatusEffect'),
	('2017-04-28 20:29:03.000000','System'),
	('2017-04-28 20:34:34.000000','Torment'),
	('2017-04-28 20:34:27.000000','Trouble'),
	('2017-04-28 20:31:41.000000','TurnBound'),
	('2017-04-28 20:32:40.000000','UntilRemoved'),
	('2017-04-28 20:32:27.000000','UseBound');

/*!40000 ALTER TABLE `game_operationtag` ENABLE KEYS */;
UNLOCK TABLES;


# Dump of table game_participant
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_participant`;

CREATE TABLE `game_participant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `created` datetime(6) NOT NULL,
  `game_id` varchar(255) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `game_participant_game_id_83350a86_fk_game_game_id` (`game_id`),
  KEY `game_participant_user_id_d99b097e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `game_participant_game_id_83350a86_fk_game_game_id` FOREIGN KEY (`game_id`) REFERENCES `game_game` (`id`),
  CONSTRAINT `game_participant_user_id_d99b097e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;



# Dump of table game_studentinfo
# ------------------------------------------------------------

DROP TABLE IF EXISTS `game_studentinfo`;

CREATE TABLE `game_studentinfo` (
  `created` datetime(6) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `backstory` varchar(255) NOT NULL,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255) NOT NULL,
  `perk_description` longtext NOT NULL,
  `perk_name` varchar(255) NOT NULL,
  `fear_description` longtext NOT NULL,
  `fear_name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

LOCK TABLES `game_studentinfo` WRITE;
/*!40000 ALTER TABLE `game_studentinfo` DISABLE KEYS */;

INSERT INTO `game_studentinfo` (`created`, `id`, `backstory`, `first_name`, `last_name`, `perk_description`, `perk_name`, `fear_description`, `fear_name`)
VALUES
	('2017-04-15 13:30:39.000000',2,'Quiet, but focused.','Polly','Bleu','Grades +2 during Dismissal Phase when in rows 2 or 3','Silent Observer','-1 turn','Mental preoccupation'),
	('2017-04-15 13:32:32.000000',3,'He\'s got a problem.. with YOU.','Sid','Devon','+5 Popularity for each Bully action played','Class Bully','',''),
	('2017-04-15 13:33:34.000000',4,'n/a','Dave','Devoix','+2 popularity for each action that generates 3 or more trouble','Charmer','',''),
	('2017-05-14 00:40:59.000000',5,'None','Joe','Schmo','None','None','None','None'),
	('2017-05-14 00:41:28.000000',6,'n/a','Gene','Kim','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:42:15.000000',7,'n/a','Fredrick','Vega','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:42:29.000000',8,'n/a','Curtis','Morrison','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:42:46.000000',9,'n/a','Marta','Castro','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:43:01.000000',10,'n/a','Tommy','Wolfe','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:43:13.000000',11,'n/a','Catherine','Alvarez','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:43:27.000000',12,'n/a','Lorena','Adams','Adams','Adams','Adams','Adams'),
	('2017-05-14 00:43:46.000000',13,'n/a','Mathilda','Dowling','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:44:03.000000',14,'n/a','Lelah','Whelan','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:44:20.000000',15,'n/a','Ha','Crooks','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:44:46.000000',16,'n/a','Rhea','Macias','n/a','n/a','n/a','n/a'),
	('2017-05-14 00:45:03.000000',17,'n/a','Fredric','Ponder','n/a','n/a','n/a','n/a');

/*!40000 ALTER TABLE `game_studentinfo` ENABLE KEYS */;
UNLOCK TABLES;



/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
