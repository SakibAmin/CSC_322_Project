-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: computer_store
-- ------------------------------------------------------
-- Server version	8.0.20

--
-- Table structure for table `registered_customers`


UNLOCK TABLES;
DROP SCHEMA IF EXISTS `computer_store`;
CREATE SCHEMA `computer_store`;
USE `computer_store`;


DROP TABLE IF EXISTS `registered_customers`;
CREATE TABLE `registered_customers` (
  `registered_id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`registered_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `registered_customers`
--

UNLOCK TABLES;
LOCK TABLES `registered_customers` WRITE;
INSERT INTO `registered_customers` VALUES (1,'Bob Jones','bobjones@gmail.com','password','114-11 134st');
UNLOCK TABLES;


--
-- Table structure for table `store_clerk`
--

DROP TABLE IF EXISTS `store_clerk`;
CREATE TABLE `store_clerk` (
  `clerk_id` int NOT NULL AUTO_INCREMENT,
  `registered_id` int DEFAULT NULL,
  PRIMARY KEY (`clerk_id`),
  KEY `registered_id` (`registered_id`),
  CONSTRAINT `store_clerk_ibfk_1` FOREIGN KEY (`registered_id`) REFERENCES `registered_customers` (`registered_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `store_clerk`
--

UNLOCK TABLES;
LOCK TABLES `store_clerk` WRITE;
UNLOCK TABLES;


--
-- Table structure for table `store_managers`
--

DROP TABLE IF EXISTS `store_managers`;
CREATE TABLE `store_managers` (
  `manager_id` int NOT NULL AUTO_INCREMENT,
  `registered_id` int DEFAULT NULL,
  PRIMARY KEY (`manager_id`),
  KEY `registered_id` (`registered_id`),
  CONSTRAINT `store_managers_ibfk_1` FOREIGN KEY (`registered_id`) REFERENCES `registered_customers` (`registered_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `store_managers`
--

UNLOCK TABLES;
LOCK TABLES `store_managers` WRITE;
UNLOCK TABLES;


--
-- Table structure for table `computer_parts_companies`
--

DROP TABLE IF EXISTS `computer_parts_companies`;
CREATE TABLE `computer_parts_companies` (
  `company_id` int NOT NULL AUTO_INCREMENT,
  `Company_Name` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `computer_parts_companies`
--

UNLOCK TABLES;
LOCK TABLES `computer_parts_companies` WRITE;
INSERT INTO `computer_parts_companies` VALUES (1,'Intel','intel@gmail.com','password'),(2,'AMD','amd@gmail.com','password'),(3,'Corsair','corsair@gmail.com','password'),(4,'G.Skill','gskill@gmail.com','password'),(5,'Crucial','crucial@gmail.com','password'),(6,'NVIDIA','nvidia@gmail.com','password'),(7,'EVGA','evga@gmail.com','password'),(8,'ASUS','asus@gmail.com','password'),(9,'AsRock','asrock@gmail.com','password'),(10,'NZXT','nzxt@gmail.com','password'),(11,'Lian Li','lianli@gmail.com','password'),(12, 'Phanteks','phanteks@gmail.com', 'password'),(13,'Cooler Master','coolermaster@gmail.com', 'password'),(14,'be quiet!','bequiet@gmail.com', 'password');
UNLOCK TABLES;

--
-- Table structure for table `cases`
--

DROP TABLE IF EXISTS `case`;
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
  PRIMARY KEY (`case_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cases_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cases`
--

UNLOCK TABLES;
LOCK TABLES `case` WRITE;
INSERT INTO `case` VALUES (1, 12, 'Phanteks Eclipse P360A ATX Mid Tower', 'ATX Mid Tower', 'Yes', 0, 5, 15, 120, 2, 2, 1, 2, 3, 'Supported', 70),(2, 3, 'Corsair Carbide Quiet Series 330R', 'ATX Mid Tower', 'Yes', 3, 4, 14, 140, 2, 2, 1, 2, 2, 'Not Supported', 106), (3, 10, 'NZXT H210i', 'Mini ITX', 'Yes', 2, 2, 12, 140, 2, 0, 1, 2, 1, 'Supported', 106), (4, 11, 'Lian Li Lancool II', 'ATX Mid Tower', 'Yes', 2, 2, 15, 140, 3, 1, 2, 3, 1, 'Supported', 110), (5, 13, 'Cooler Master Cosmos C700P Black Edition', 'Full ATX Tower', 'Yes', 2, 7, 20, 140, 3, 3, 1, 1, 2, 'Supported', 250), (6, 14, 'be quiet! Dark Pro 900', 'Full ATX Tower', 'Yes', 2, 8, 20, 140, 3, 3, 1, 2, 2, 'Supported', 270);
UNLOCK TABLES;

--
-- Table structure for table `cpu`
--

DROP TABLE IF EXISTS `cpu`;
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
  PRIMARY KEY (`cpu_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `cpu_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `cpu`
--

UNLOCK TABLES;
LOCK TABLES `cpu` WRITE;
INSERT INTO `cpu` VALUES (1,1,'Intel Core i3-10100',4,'3.6GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',115),(2,1,'Intel Core i5-10400',6,'2.9GHz','4.3GHz','Intel UHD Graphics 630','LGA1200','Yes',150),(3,1,'Intel Core i7-10700K',8,'3.8GHz','5.1GHz','Intel UHD Graphics 630','LGA1200','No',315),(4,1,'Intel Core i9-10900K',10,'3.7GHz','5.3GHz','Intel UHD Graphics 630','LGA1200','No',436),(5,2,'AMD Ryzen 3 3200G',4,'3.6GHz','4 GHz','Radeon Vega 8','AM4','Yes',100),(6,2,'AMD Ryzen 5 3600',6,'3.6GHz','4.2GHz','N/A','AM4','Yes',200),(7,2,'AMD Ryzenn 7 3700X',8,'3.6GHz','4.4GHz','N/A','AM4','Yes',320),(8,2,'AMD Threadripper 3990X',64,'2.9GHz','4.3Ghz','N/A','sTRX4','No',3959);
UNLOCK TABLES;


--
-- Table structure for table `delivery_companies`
--

DROP TABLE IF EXISTS `delivery_companies`;
CREATE TABLE `delivery_companies` (
  `Company_Name` varchar(255) DEFAULT NULL,
  `email` varchar(255) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `delivery_companies`
--

UNLOCK TABLES;
LOCK TABLES `delivery_companies` WRITE;
UNLOCK TABLES;

--
-- Table structure for table `gpu`
--

DROP TABLE IF EXISTS `gpu`;
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
  PRIMARY KEY (`gpu_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `gpu_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `gpu`
--

UNLOCK TABLES;
LOCK TABLES `gpu` WRITE;
INSERT INTO `gpu` VALUES (1,6,'NVIDIA Founders Edition Gefore RTX 3060',8,'1410','1670','PClex16',242,1,3,400),(2,6,'NVIDIA Founders Edition Gefore RTX 3070',8,'1500','1730','PClex16',242,1,3,600),(4,6,'NVIDIA Founders Edition Gefore RTX 3080',10,'1440','1710','PClex16',285,1,3,800),(5,7,'EVGA Gefore RTX 3060 12GB ',12,'1320','1882','PClex16',202,1,3,389),(6,8,'ASUS Gefore RTX 3070 8 GB ',8,'1500','14000','PClex16',300,2,3,749),(7,8,'ASUS Gefore RTX 3080 10GB',10,'1440','19500','PClex16',300,2,3,2799);
UNLOCK TABLES;


--
-- Table structure for table `motherboard`
--

DROP TABLE IF EXISTS `motherboard`;
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
  PRIMARY KEY (`motherboard_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `motherboard_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `motherboard`
--

UNLOCK TABLES;
LOCK TABLES `motherboard` WRITE;
INSERT INTO `motherboard` VALUES (1,8,'ASUS ROG STRIX B550-F','ATX','AM4','DDR4',4,'Yes','Yes',6,2,1,'Yes','Yes',200),(2,8,'ASUS ROG STRIX Z490-E','ATX','LGA1200','DDR4',4,'Yes','Yes',6,2,1,'Yes','Yes',300),(3,9,'ASRock B450M PRO4','Micro-ATX','AM4','DDR4',4,'Yes','Yes',4,2,1,'No','No',80),(5,9,'AsRock B460M Pro4','ATX','LGA1200','DDR4',4,'Yes','Yes',6,2,1,'No','Yes',154),(6,8,'ASUS ROG Zenith II EXTREME ALPHA','E-ATX','sTRX4','DDR4',8,'Yes','Yes',8,2,2,'Yes','Yess',871);
UNLOCK TABLES;


--
-- Table structure for table `ram`
--

DROP TABLE IF EXISTS `ram`;
CREATE TABLE `ram` (
  `ram_id` int NOT NULL AUTO_INCREMENT,
  `company_id` int DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `type` varchar(255) DEFAULT NULL,
  `speed` int DEFAULT NULL,
  `modules` varchar(255) DEFAULT NULL,
  `rgb` varchar(255) DEFAULT NULL,
  `price` int DEFAULT NULL,
  PRIMARY KEY (`ram_id`),
  KEY `company_id` (`company_id`),
  CONSTRAINT `ram_ibfk_1` FOREIGN KEY (`company_id`) REFERENCES `computer_parts_companies` (`company_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `ram`
--

UNLOCK TABLES;
LOCK TABLES `ram` WRITE;
INSERT INTO `ram` VALUES (1,3,'Corsair Vengeance RGB Pro 16GB','DDR4',3200,'2x8','Yes',110),(2,3,'Corsair Vengeance RGB Pro 32GB','DDR4',3200,'2x16','Yes',300),(3,4,'G.Skill Aegis 16GB','DDR4',3000,'2x8','No',80),(4,4,'G.Skill Tridant Z RGB 16GB','DDR4',3200,'2x8','Yes',115),(5,4,'G.Skill Tridant Z RGB 128GB','DDR4',4000,'4x32','Yes',880),(6,5,'Crucial Ballistix 32GB','DDR4',3200,'2x16','No',176);
UNLOCK TABLES;