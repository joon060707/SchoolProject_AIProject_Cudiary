-- MySQL dump 10.13  Distrib 8.0.40, for Win64 (x86_64)
--
-- Host: localhost    Database: aip
-- ------------------------------------------------------
-- Server version	8.0.43

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `plant`
--

DROP TABLE IF EXISTS `plant`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `plant` (
  `plant_id` int NOT NULL,
  `plant_name` varchar(100) DEFAULT NULL,
  `last_stage` varchar(30) DEFAULT NULL,
  `note` varchar(200) DEFAULT NULL,
  `start_date` datetime DEFAULT NULL,
  PRIMARY KEY (`plant_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plant`
--

LOCK TABLES `plant` WRITE;
/*!40000 ALTER TABLE `plant` DISABLE KEYS */;
INSERT INTO `plant` VALUES (20,'warsdf','Seedling','No description provided for New Plant 0','2025-12-01 00:00:00'),(21,'weqrf','Seedling','No description provided for New Plant 0','2025-12-01 00:00:00'),(22,'ewqtwar','Seedling','ae','2025-11-01 00:00:00'),(23,'ertywertert','Seedling','No description provided for New Plant 0','2025-11-14 00:00:00'),(24,'mask','Seedling','aser','2025-11-22 00:00:00'),(25,'wow','Seedling','ww','2025-11-30 00:00:00'),(26,'test1','Seedling','No description provided for New Plant 26','2025-09-17 00:00:00'),(27,'colortest','Seedling','No description provided for New Plant 27','2025-11-11 00:00:00'),(28,'imagetest','Seedling','No description provided for New Plant 28','2025-11-11 00:00:00'),(29,'testtest','Seedling','I\'m editing this\nhaha','2025-11-22 00:00:00'),(30,'testests','Seedling','No description provided for New Plant 0','2025-11-22 00:00:00'),(31,'mymyplant','Seedling','fruites','2025-09-17 00:00:00'),(32,'tinyplant','Seedling','flower','2025-09-17 00:00:00'),(33,'New Plant','Seedling','No description provided for New Plant 0','2025-12-06 00:00:00'),(34,'New Plant','Seedling','Consider checking nutrient levels, water, and light exposure.\ntt','2025-12-06 00:00:00'),(35,'last','Seedling','ee','2025-09-20 00:00:00'),(36,'JPlant','Seedling','fruits!!\ntea','2025-09-17 00:00:00'),(37,'PhotoPlant','Seedling','image test','2025-09-20 00:00:00'),(38,'hrrr','Seedling','bbb\n\nㄱ\nㄴ\n\n...ㄷ\nㄹae','2025-10-06 00:00:00');
/*!40000 ALTER TABLE `plant` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-07  4:07:46
