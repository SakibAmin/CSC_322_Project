-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: computer_store
-- ------------------------------------------------------
-- Server version	8.0.20

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
-- Table structure for table `computer_parts_companies`
--

DROP TABLE IF EXISTS `computer_parts_companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `computer_parts_companies` (
  `company_id` int NOT NULL AUTO_INCREMENT,
  `Company_Name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `pending_warnings` int DEFAULT NULL,
  `standing_warnings` int DEFAULT NULL,
  `funds` int DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computer_parts_companies`
--

LOCK TABLES `computer_parts_companies` WRITE;
/*!40000 ALTER TABLE `computer_parts_companies` DISABLE KEYS */;
INSERT INTO `computer_parts_companies` VALUES (1,'Intel','intel@gmail.com','password',3,3,0),(2,'AMD','amd@gmail.com','password',NULL,NULL,118218),(3,'Corsair','corsair@gmail.com','password',NULL,NULL,NULL),(4,'G.Skill','gskill@gmail.com','password',NULL,NULL,NULL),(5,'Crucial','crucial@gmail.com','password',NULL,NULL,NULL),(6,'NVIDIA','nvidia@gmail.com','password',NULL,NULL,NULL),(7,'EVGA','evga@gmail.com','password',NULL,NULL,NULL),(8,'ASUS','asus@gmail.com','password',NULL,NULL,NULL),(9,'AsRock','asrock@gmail.com','password',NULL,NULL,NULL),(10,'NZXT','nzxt@gmail.com','password',NULL,NULL,NULL),(11,'Lian Li','lianli@gmail.com','password',NULL,NULL,NULL),(12,'Seagate','seagate@gmail.com','password',NULL,NULL,NULL),(13,'Samsung','samsung@gmail.com','password',NULL,NULL,NULL),(14,'Kingston','kingston@gmail.com','password',NULL,NULL,NULL),(15,'Cooler Master','coolermaster@gmail.com','password',NULL,NULL,NULL),(16,'Arctic','arctic@gmail.com','password',NULL,NULL,NULL),(17,'Noctua','noctua@gmail.com','password',NULL,NULL,NULL);
/*!40000 ALTER TABLE `computer_parts_companies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-13  1:45:30
