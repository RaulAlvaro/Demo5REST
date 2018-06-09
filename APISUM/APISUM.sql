-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema APISUM
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema APISUM
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `APISUM` DEFAULT CHARACTER SET utf8 ;
USE `APISUM` ;

-- -----------------------------------------------------
-- Table `APISUM`.`Alumno`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `APISUM`.`Alumno` (
  `codigoAlumno` INT NOT NULL,
  `nombresAlumno` VARCHAR(45) NOT NULL,
  `apellidosAlumno` VARCHAR(45) NOT NULL,
  `facultad` VARCHAR(45) NOT NULL,
  `escuela` VARCHAR(45) NOT NULL,
  `sexo` VARCHAR(45) NULL,
  `telefono` VARCHAR(45) NULL,
  `direccion` VARCHAR(45) NULL,
  PRIMARY KEY (`codigoAlumno`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
