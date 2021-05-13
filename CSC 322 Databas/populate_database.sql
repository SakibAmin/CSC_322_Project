
UNLOCK TABLES;
DROP SCHEMA IF EXISTS `computer_store`;
CREATE SCHEMA `computer_store`;
USE `computer_store`;

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
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `case`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `case` (
  `case_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `case_type` varchar(255) DEFAULT NULL,
  `side_panel` varchar(255) DEFAULT NULL,
  `external_bay` int DEFAULT NULL,
  `internal_bay` int DEFAULT NULL,
  `max_gpu_size` int DEFAULT NULL,
  `max_fan_size` int DEFAULT NULL,
  `num_front_fan` int DEFAULT NULL,
  `num_top_fan` int DEFAULT NULL,
  `num_exhaust_fan` int DEFAULT NULL,
  `num_fan_included` int DEFAULT NULL,
  `max_radiator` int DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`case_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `case_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cases`
--

LOCK TABLES `case` WRITE;
/*!40000 ALTER TABLE `case` DISABLE KEYS */;
INSERT INTO `case` VALUES (1,10,'NZXT H510','ATX','Tempered Glass',0,2,381,140,2,1,1,1,280,'No',80,20,14,1120),(2,11,'Lian Li PC-O11 Dynamic','E-ATX','Tempered Glass',0,2,420,140,3,2,1,0,420,'No',160,22,22,3520),(3,3,'Corsair iCUE 4000X','ATX','Tempered Glass',0,2,360,140,3,2,1,3,420,'Yes',135,32,12,1620),(4,3,'Corsair Crystal 280X','Micro-ATX','Tempered Glass',0,2,300,140,2,2,1,1,280,'No',106,12,13,1378);
/*!40000 ALTER TABLE `case` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:05

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
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `computer_parts_companies`
--

LOCK TABLES `computer_parts_companies` WRITE;
/*!40000 ALTER TABLE `computer_parts_companies` DISABLE KEYS */;
INSERT INTO `computer_parts_companies` VALUES (1,'Intel','intel@gmail.com','password'),(2,'AMD','amd@gmail.com','password'),(3,'Corsair','corsair@gmail.com','password'),(4,'G.Skill','gskill@gmail.com','password'),(5,'Crucial','crucial@gmail.com','password'),(6,'NVIDIA','nvidia@gmail.com','password'),(7,'EVGA','evga@gmail.com','password'),(8,'ASUS','asus@gmail.com','password'),(9,'AsRock','asrock@gmail.com','password'),(10,'NZXT','nzxt@gmail.com','password'),(11,'Lian Li','lianli@gmail.com','password'),(12,'Seagate','seagate@gmail.com','password'),(13,'Samsung','samsung@gmail.com','password'),(14,'Kingston','kingston@gmail.com','password'),(15,'Cooler Master','coolermaster@gmail.com','password'),(16,'Arctic','arctic@gmail.com','password'),(17,'Noctua','noctua@gmail.com','password');
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

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `cooler`
--

DROP TABLE IF EXISTS `cooler`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cooler` (
  `cooler_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `fan_rpm` varchar(255) DEFAULT NULL,
  `type_of_cooler` varchar(255) DEFAULT NULL,
  `Radiator` int DEFAULT NULL,
  `socket` varchar(255) DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`cooler_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cooler_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cooler`
--

LOCK TABLES `cooler` WRITE;
/*!40000 ALTER TABLE `cooler` DISABLE KEYS */;
INSERT INTO `cooler` VALUES (1,15,'Cooler Master Hyper 212','650-2000RPM','Air',0,'All','Yes',50,32,45,2250),(2,10,'NZXT Kraken Z73','500-1800 RPM','Liquid',360,'All','Yes',280,23,60,16800),(3,10,'NZXT Kraken X63','500-2000RPM','Liquid',280,'All','Yes',150,34,44,6600),(4,16,'Arctic Liquid Freezer II','200-1700RPM','Liquid',420,'All','No',348,44,13,4524),(5,17,'Noctua NH-U14S TR4 SP3','300-1500RPM','Air',0,'sTRX4','No',90,12,21,1890);
/*!40000 ALTER TABLE `cooler` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `cpu`
--

DROP TABLE IF EXISTS `cpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cpu` (
  `cpu_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `number_of_cores` int DEFAULT NULL,
  `clock_speed` varchar(225) DEFAULT NULL,
  `boosted_clock_speed` varchar(255) DEFAULT NULL,
  `integrated_graphics` varchar(255) DEFAULT NULL,
  `socket` varchar(255) DEFAULT NULL,
  `cooler` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`cpu_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cpu_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cpu`
--

LOCK TABLES `cpu` WRITE;
/*!40000 ALTER TABLE `cpu` DISABLE KEYS */;
INSERT INTO `cpu` VALUES (1,1,'Intel Core i3-10100',4,'3.6GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',115,20,15,1725),(2,1,'Intel Core i5-10400',6,'2.9GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',150,45,16,2400),(3,1,'Intel Core i7-10700K',8,'3.8GHz','5.1GHz','Intel UHD Graphics 630','LGA1200','No',315,65,55,17325),(4,1,'Intel Core i9-10900K',10,'3.7GHz','5.3GHz','Intel UHD Graphics 630','LGA1200','No',436,30,5,2180),(5,2,'AMD Ryzen 3 3200G',4,'3.6GHz','4 GHz','Radeon Vega 8','AM4','Yes',100,22,12,1200),(6,2,'AMD Ryzen 5 3600',6,'3.6GHz','4.2GHz','N/A','AM4','Yes',200,34,44,8800),(7,2,'AMD Ryzenn 7 3700X',8,'3.6GHz','4.4GHz','N/A','AM4','Yes',320,12,66,21120),(8,2,'AMD Threadripper 3990X',64,'2.9GHz','4.3Ghz','N/A','sTRX4','No',3959,34,22,87098);
/*!40000 ALTER TABLE `cpu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `delivery_companies`
--

DROP TABLE IF EXISTS `delivery_companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `delivery_companies` (
  `delivery_id` int NOT NULL AUTO_INCREMENT,
  `Company_Name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`delivery_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `delivery_companies`
--

LOCK TABLES `delivery_companies` WRITE;
/*!40000 ALTER TABLE `delivery_companies` DISABLE KEYS */;
INSERT INTO `delivery_companies` VALUES (1,'UPS','ups@gmail.com','password'),(2,'FedEx','fedex@gmail.com','password');
/*!40000 ALTER TABLE `delivery_companies` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `gpu`
--

DROP TABLE IF EXISTS `gpu`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `gpu` (
  `gpu_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `memory` int DEFAULT NULL,
  `clock_speed` varchar(255) DEFAULT NULL,
  `boosted_clock_speed` varchar(255) DEFAULT NULL,
  `interface` varchar(255) DEFAULT NULL,
  `length` int DEFAULT NULL,
  `hdmi_ports` int DEFAULT NULL,
  `display_ports` int DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`gpu_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `gpu_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `gpu`
--

LOCK TABLES `gpu` WRITE;
/*!40000 ALTER TABLE `gpu` DISABLE KEYS */;
INSERT INTO `gpu` VALUES (1,6,'NVIDIA Founders Edition Gefore RTX 3060',8,'1410','1670','PClex16',242,1,3,400,12,22,8800),(2,6,'NVIDIA Founders Edition Gefore RTX 3070',8,'1500','1730','PClex16',242,1,3,600,10,33,19800),(4,6,'NVIDIA Founders Edition Gefore RTX 3080',10,'1440','1710','PClex16',285,1,3,800,9,44,35200),(5,7,'EVGA Gefore RTX 3060 12GB ',12,'1320','1882','PClex16',202,1,3,389,8,55,21395),(6,8,'ASUS Gefore RTX 3070 8 GB ',8,'1500','14000','PClex16',300,2,3,749,6,33,24717),(7,8,'ASUS Gefore RTX 3080 10GB',10,'1440','19500','PClex16',300,2,3,2799,7,44,123156);
/*!40000 ALTER TABLE `gpu` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:05

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
-- Table structure for table `motherboard`
--

DROP TABLE IF EXISTS `motherboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `motherboard` (
  `motherboard_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `form_factor` varchar(255) DEFAULT NULL,
  `socket` varchar(255) DEFAULT NULL,
  `memory_type` varchar(255) DEFAULT NULL,
  `memory_slots` int DEFAULT NULL,
  `pci_16` varchar(255) DEFAULT NULL,
  `ethernet` varchar(255) DEFAULT NULL,
  `sata` int DEFAULT NULL,
  `usb_2` int DEFAULT NULL,
  `usb_3` int DEFAULT NULL,
  `wireless` varchar(255) DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`motherboard_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `motherboard_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `motherboard`
--

LOCK TABLES `motherboard` WRITE;
/*!40000 ALTER TABLE `motherboard` DISABLE KEYS */;
INSERT INTO `motherboard` VALUES (1,8,'ASUS ROG STRIX B550-F','ATX','AM4','DDR4',4,'Yes','Yes',6,2,1,'Yes','Yes',200,33,44,8800),(2,8,'ASUS ROG STRIX Z490-E','ATX','LGA1200','DDR4',4,'Yes','Yes',6,2,1,'Yes','Yes',300,44,32,9600),(3,9,'ASRock B450M PRO4','Micro-ATX','AM4','DDR4',4,'Yes','Yes',4,2,1,'No','No',80,13,56,4480),(5,9,'AsRock B460M Pro4','ATX','LGA1200','DDR4',4,'Yes','Yes',6,2,1,'No','Yes',154,45,34,5236),(6,8,'ASUS ROG Zenith II EXTREME ALPHA','E-ATX','sTRX4','DDR4',8,'Yes','Yes',8,2,2,'Yes','Yess',871,34,47,40937);
/*!40000 ALTER TABLE `motherboard` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `powersupply`
--

DROP TABLE IF EXISTS `powersupply`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `powersupply` (
  `powersupply_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `form_factor` varchar(255) DEFAULT NULL,
  `efficency` varchar(255) DEFAULT NULL,
  `wattage` int DEFAULT NULL,
  `modular` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`powersupply_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `powersupply_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `powersupply`
--

LOCK TABLES `powersupply` WRITE;
/*!40000 ALTER TABLE `powersupply` DISABLE KEYS */;
INSERT INTO `powersupply` VALUES (1,3,'Corsair RM','ATX','80+ Gold',750,'Full',80,33,35,2800),(2,7,'EVGA SuperNova GA','ATX','80+ Gold',650,'Full',80,37,44,3520),(3,3,'Corsair Axi','ATX','80+ Plat',1600,'Full',120,32,63,7560),(4,3,'Corsair CXM','ATX','80+ Bronze',550,'Semi',55,41,13,715);
/*!40000 ALTER TABLE `powersupply` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `ram`
--

DROP TABLE IF EXISTS `ram`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ram` (
  `ram_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `speed` int DEFAULT NULL,
  `modules` varchar(255) DEFAULT NULL,
  `sticks` int DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`ram_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `ram_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ram`
--

LOCK TABLES `ram` WRITE;
/*!40000 ALTER TABLE `ram` DISABLE KEYS */;
INSERT INTO `ram` VALUES (1,3,'Corsair Vengeance RGB Pro 16GB','DDR4',3200,'2x8',2,'Yes',110,100,33,3630),(2,3,'Corsair Vengeance RGB Pro 32GB','DDR4',3200,'2x16',2,'Yes',300,44,24,7200),(3,4,'G.Skill Aegis 16GB','DDR4',3000,'2x8',2,'No',80,34,56,4480),(4,4,'G.Skill Tridant Z RGB 16GB','DDR4',3200,'2x8',2,'Yes',115,55,72,8280),(5,4,'G.Skill Tridant Z RGB 128GB','DDR4',4000,'4x32',4,'Yes',880,21,11,9680),(6,5,'Crucial Ballistix 32GB','DDR4',3200,'2x16',2,'No',176,55,89,15664);
/*!40000 ALTER TABLE `ram` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `registered_customers`
--

DROP TABLE IF EXISTS `registered_customers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `registered_customers` (
  `registered_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`registered_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `registered_customers`
--

LOCK TABLES `registered_customers` WRITE;
/*!40000 ALTER TABLE `registered_customers` DISABLE KEYS */;
INSERT INTO `registered_customers` VALUES (1,'Bob Jones','bobjones@gmail.com','password','114-11 134st'),(2,'John Doe','johndoe@gmail.com','password','114-11 134st');
/*!40000 ALTER TABLE `registered_customers` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:05

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
-- Table structure for table `storage`
--

DROP TABLE IF EXISTS `storage`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `storage` (
  `storage_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `capacity` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `form_factor` varchar(255) DEFAULT NULL,
  `Interface` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  `in_stock` int DEFAULT NULL,
  `sold` int DEFAULT NULL,
  `total_profit` int DEFAULT NULL,
  PRIMARY KEY (`storage_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `storage_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `storage`
--

LOCK TABLES `storage` WRITE;
/*!40000 ALTER TABLE `storage` DISABLE KEYS */;
INSERT INTO `storage` VALUES (1,12,'Seagate Barracuda Compute ','2TB','7200RPM','3.5','SATA 6 Gbb/s',53,33,34,1802),(2,13,'Samsung 860 Evo ','1 TB','SSD','2.5','SATA 6 Gbb/s',110,32,22,2420),(3,13,'Samsung 980 Pro','1 TB','SSD','M.2','SATA 6 Gbb/s',200,12,8,1600),(4,14,'Kingston A400 240','240 GB','SSD','2.5','SATA 6 Gbb/s',40,13,12,480);
/*!40000 ALTER TABLE `storage` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

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
-- Table structure for table `store_clerk`
--

DROP TABLE IF EXISTS `store_clerk`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_clerk` (
  `clerk_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`clerk_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_clerk`
--

LOCK TABLES `store_clerk` WRITE;
/*!40000 ALTER TABLE `store_clerk` DISABLE KEYS */;
INSERT INTO `store_clerk` VALUES (1,'Lebron James','lebronjames@gmail.com','password'),(2,'Kyrie Irving','kyrieirving@gmail.com','password');
/*!40000 ALTER TABLE `store_clerk` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:05


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
-- Table structure for table `store_manager`
--

DROP TABLE IF EXISTS `store_manager`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `store_manager` (
  `manager_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`manager_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `store_manager`
--

LOCK TABLES `store_manager` WRITE;
/*!40000 ALTER TABLE `store_manager` DISABLE KEYS */;
INSERT INTO `store_manager` VALUES (1,'Adam Silver','nba@gmail.com','password');
/*!40000 ALTER TABLE `store_manager` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-05-11 17:00:04

DROP TABLE IF EXISTS `discussion`;
CREATE TABLE `discussion` (
  `discussion_id` int NOT NULL AUTO_INCREMENT,
  `part_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`discussion_id`)
);

-- UNLOCK TABLES;
-- LOCK TABLES `discussion` WRITE;
INSERT INTO discussion (part_name)
SELECT name FROM computer_store.case
UNION
SELECT name FROM computer_store.cooler
UNION
SELECT name FROM computer_store.cpu
UNION
SELECT name FROM computer_store.gpu
UNION
SELECT name FROM computer_store.motherboard
UNION
SELECT name FROM computer_store.powersupply
UNION
SELECT name FROM computer_store.ram
UNION
SELECT name FROM computer_store.storage;
-- UNLOCK TABLES;


--   FOREIGN KEY (discussion_id) REFERENCES discussion(discussion_id),
--   FOREIGN KEY (registered_id) REFERENCES registered_customers(registered_id),

DROP TABLE IF EXISTS `comment`;
CREATE TABLE `comment` (
  `comment_id` int NOT NULL AUTO_INCREMENT,
  `discussion_id` int DEFAULT NULL,
  `registered_id` int DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`comment_id`),
  KEY `discussion_id` (`discussion_id`), 
  KEY `registered_id` (`registered_id`),
  CONSTRAINT `discussion_ibfk_1` FOREIGN KEY (`discussion_id`) REFERENCES `discussion` (`discussion_id`),
  CONSTRAINT `registered_customers_ibfk_1` FOREIGN KEY (`registered_id`) REFERENCES `registered_customers` (`registered_id`)
);

LOCK TABLES `comment` WRITE;
INSERT INTO `comment` VALUES (1, 1, 1, 'hello i like this product, very nice!!1'), (2, 1, 1, 'it is me again!! i love this item'), (3, 1, 2, 'same!');
UNLOCK TABLES;

DROP TABLE IF EXISTS `taboo`;
CREATE TABLE `taboo` (
  `taboo_id` int NOT NULL AUTO_INCREMENT,
  `word` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`taboo_id`)
);

LOCK TABLES `taboo` WRITE;
INSERT INTO `taboo` VALUES (1, 'badword'),(2, 'poopy'),(3, 'nerd'),(4, 'supernerd'),(5, 'stupid'),(6, 'meanie');
UNLOCK TABLES;

DROP TABLE IF EXISTS `complain`;
CREATE TABLE `complain` (
  `complain_id` int NOT NULL AUTO_INCREMENT,
  `complainee_email` varchar(255) DEFAULT NULL,
  `complainant_id` int DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`complain_id`),
  KEY `complainant_id` (`complainant_id`), 
  CONSTRAINT complainant_ibfk_1 FOREIGN KEY (complainant_id) REFERENCES registered_customers(registered_id)
);

LOCK TABLES `complain` WRITE;
INSERT INTO `complain` VALUES (1, 'johndoe@gmail.com', 1, 'i dont like what they commented'),(2, 'johndoe@gmail.com', 1, 'i dont like them'),(3, 'johndoe@gmail.com', 1, 'hate him'), (4, 'ups@gmail.com', 1, 'bad service'), (5, 'lebronjames@gmail.com', 1, 'bad clerk'), (6, 'intel@gmail.com', 1, 'faulty item');
UNLOCK TABLES;

DROP TABLE IF EXISTS `appeal`;
CREATE TABLE `appeal` (
  `appeal_id` int NOT NULL AUTO_INCREMENT,
  `complain_id` int NOT NULL,
--   `registered_id` int DEFAULT NULL,
  `reason` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`appeal_id`),
--   KEY `registered_id` (`registered_id`),   
  KEY `complain_id` (`complain_id`), 
--   CONSTRAINT registered_id_ibfk_1 FOREIGN KEY (registered_id) REFERENCES registered_customers(registered_id),
  CONSTRAINT complain_id_ibfk_1 FOREIGN KEY (complain_id) REFERENCES complain(complain_id)
);

LOCK TABLES `appeal` WRITE;
INSERT INTO `appeal` VALUES (1, 1, 'i did not mean to say it like that, i apologize'),(2, 2, 'i dont deserve this!');
UNLOCK TABLES;