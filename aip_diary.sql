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
-- Table structure for table `diary`
--

DROP TABLE IF EXISTS `diary`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `diary` (
  `id` int NOT NULL,
  `date` datetime DEFAULT NULL,
  `plant_id` int DEFAULT NULL,
  `unit` varchar(30) DEFAULT NULL,
  `stage` varchar(30) DEFAULT NULL,
  `organ_type` varchar(30) DEFAULT NULL,
  `diagnosis` varchar(30) DEFAULT NULL,
  `diagnosis_detail` varchar(511) DEFAULT NULL,
  `chlorophyll_content` varchar(30) DEFAULT NULL,
  `measurement` int DEFAULT NULL,
  `note` varchar(511) DEFAULT NULL,
  `note2` varchar(511) DEFAULT NULL,
  `img` varchar(511) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `plant_id` (`plant_id`),
  CONSTRAINT `diary_ibfk_1` FOREIGN KEY (`plant_id`) REFERENCES `plant` (`plant_id`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `diary`
--

LOCK TABLES `diary` WRITE;
/*!40000 ALTER TABLE `diary` DISABLE KEYS */;
INSERT INTO `diary` VALUES (33,'2025-12-01 00:00:00',20,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',29,'No description provided for New Plant 0','temp','http://localhost:3000/upload/1764586462510-V100_4_3_1_5_1_1_1_6_0_0_20220728_14518_20240422191141.jpg_borders.png'),(34,'2025-12-01 00:00:00',21,'Single organ','Flowering','Flower','Too early flowering','Check the plant\'s environment conditions.','Normal',20,'No description provided for New Plant 0','temp','http://localhost:3000/upload/1764586729610-test2_1025.jpg_borders.png'),(35,'2025-12-01 00:00:00',22,'Whole plant','Vegetative','Leaf','Healthy','You\'re looking at the whole plant(s). You may need to see them closer.','Normal',61,'ae','temp','http://localhost:3000/upload/1764587606945-V100_4_3_1_5_1_1_1_4_0_0_20220716_5057_20240422190110.jpg_borders.png'),(36,'2025-12-01 00:00:00',23,'Whole plant','Vegetative','Leaf','Healthy','You\'re looking at the whole plant(s). You may need to see them closer.','Normal',103,'No description provided for New Plant 0','temp','http://localhost:3000/upload/1764587785291-10_20201229_1822882.JPG_borders.png'),(37,'2025-12-01 00:00:00',24,'Single organ','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',0,'Consider checking nutrient levels, water, and light exposure.','temp','http://localhost:3000/upload/1764588118203-10_20201005_200858.JPGgreen_mask.png_borders.png'),(38,'2025-12-02 00:00:00',24,'Single organ','Fruiting','Fruit','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',20,'aser','temp','http://localhost:3000/upload/1764588174577-10_20201229_1822825.JPG_green_mask.png_borders.png'),(39,'2025-12-01 00:00:00',25,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',509,'ww','temp','http://localhost:3000/upload/1764588431904-test.png_borders.png'),(40,'2025-09-25 00:00:00',26,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'No issues detected.','temp','http://localhost:3000/upload/1764588970197-test1_0925.JPG_borders.png'),(41,'2025-10-25 00:00:00',26,'Single organ','Flowering','Flower','Healthy','No issues detected.','High',112,'No issues detected.','temp','http://localhost:3000/upload/1764588998999-test2_1025.jpg_borders.png'),(42,'2025-11-06 00:00:00',26,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',77,'Harvesting time is appropriate.','temp','http://localhost:3000/upload/1764589016441-test3_1106.JPG_borders.png'),(43,'2025-12-01 00:00:00',27,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','Normal',75,'No issues detected.','temp','http://localhost:3000/upload/1764589158346-asdf.JPG_borders.png'),(44,'2025-12-02 00:00:00',27,'Single organ','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',0,'Consider checking nutrient levels, water, and light exposure.','temp','http://localhost:3000/upload/1764589196173-asdf.JPG_borders.png'),(45,'2025-11-22 00:00:00',28,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',77,'Harvesting time is appropriate.','temp','http://localhost:3000/upload/1764589371205-pseudocapture.png_borders.png'),(46,'2025-11-23 00:00:00',28,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','Normal',77,'No issues detected.','temp','http://localhost:3000/upload/1764589442805-pseudocapture.png_borders.png'),(47,'2025-11-24 00:00:00',29,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'I\'m editing this\nhaha','temp','http://localhost:3000/upload/1764589538381-test1_0925.JPG_borders.png'),(48,'2025-11-26 00:00:00',30,'Single organ','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',0,'Consider checking nutrient levels, water, and light exposure.','temp','http://localhost:3000/upload/1764589629050-asdf.JPG_borders.png'),(49,'2025-09-25 00:00:00',31,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'No issues detected.','temp','http://localhost:3000/upload/1764590700614-test1_0925.JPG_borders.png'),(50,'2025-10-25 00:00:00',31,'Single organ','Flowering','Flower','Healthy','No issues detected.','High',112,'next','temp','http://localhost:3000/upload/1764590725190-test2_1025.jpg_borders.png'),(51,'2025-11-06 00:00:00',31,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',32,'fruites','temp','http://localhost:3000/upload/1764590744736-test3_1106.JPG_borders.png'),(52,'2025-09-25 00:00:00',32,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'No issues detected.','temp','http://localhost:3000/upload/1764591069371-test1_0925.JPG_borders.png'),(53,'2025-10-25 00:00:00',32,'Single organ','Flowering','Flower','Healthy','No issues detected.','High',112,'flower','temp','http://localhost:3000/upload/1764591088858-test2_1025.jpg_borders.png'),(54,'2025-11-06 00:00:00',32,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',77,'fruit','temp','http://localhost:3000/upload/1764591106145-test3_1106.JPG_borders.png'),(57,'2025-12-06 00:00:00',33,'Single organ','Fruiting','Fruit','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',0,'Consider checking nutrient levels, water, and light exposure.','temp','http://localhost:3000/upload/1765016411302-1765016411289capture.png_borders.png'),(58,'2025-12-06 00:00:00',34,'Single organ','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',200,'Consider checking nutrient levels, water, and light exposure.\ntt','temp','http://localhost:3000/upload/1765016433044-bg2.jpg_borders.png'),(59,'2025-09-25 00:00:00',35,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'start','temp','http://localhost:3000/upload/1765017659400-test1_0925.JPG_borders.png'),(60,'2025-10-04 00:00:00',35,'Whole plant','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',52,'ee','temp','http://localhost:3000/upload/1765018112132-1765018112121capture.png_borders.png'),(61,'2025-09-25 00:00:00',36,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','High',122,'myplant','temp','http://localhost:3000/upload/1765030166556-test1_0925.JPG_borders.png'),(62,'2025-10-25 00:00:00',36,'Single organ','Flowering','Flower','Healthy','No issues detected.','High',112,'flower','temp','http://localhost:3000/upload/1765030197528-test2_1025.jpg_borders.png'),(63,'2025-11-06 00:00:00',36,'Single organ','Fruiting','Fruit','Healthy','Harvesting time is appropriate.','Normal',80,'fruits!!\ntea','temp','http://localhost:3000/upload/1765030216615-test3_1106.JPG_borders.png'),(64,'2025-09-25 00:00:00',37,'Single organ','Vegetative','Leaf','Healthy','No issues detected.','Normal',83,'image test','temp','http://localhost:3000/upload/1765030890055-1765030890047capture.png_borders.png'),(65,'2025-10-10 00:00:00',38,'Single organ','Vegetative','Leaf','Chlorophyll deficiency','Consider checking nutrient levels, water, and light exposure.','Low',0,'bbb\n\nㄱ\nㄴ\n\n...ㄷ\nㄹae','temp','http://localhost:3000/upload/1765031177862-asdf.JPG_borders.png');
/*!40000 ALTER TABLE `diary` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-12-07  4:07:45
