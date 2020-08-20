CREATE DATABASE `pypos` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;

CREATE TABLE `tblemployees` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `number` varchar(45) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rid`),
  UNIQUE KEY `rid_UNIQUE` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tblsettings` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `key` varchar(45) NOT NULL,
  `value` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`rid`,`key`),
  UNIQUE KEY `rid_UNIQUE` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `tblusers` (
  `rid` int NOT NULL AUTO_INCREMENT,
  `userName` varchar(45) DEFAULT NULL,
  `userPwd` longtext,
  PRIMARY KEY (`rid`),
  UNIQUE KEY `rid_UNIQUE` (`rid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
