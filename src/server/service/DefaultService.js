'use strict';


/**
 * Submit a login with user credential payload for group member with existing AI service agent
 *
 * name Object 
 * password Object 
 * inviterDefaultAppId Object  (optional)
 * inviterUserRole Object  (optional)
 * no response value expected for this operation
 **/
exports.execute_loginPOST = function(name,password,inviterDefaultAppId,inviterUserRole) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Load logout payload as group member for existing AI service agent
 *
 * no response value expected for this operation
 **/
exports.execute_logoutPOST = function() {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Commit a new sign-up application payload for group member with new AI service agent onto Researcher Hub
 *
 * avatar Object 
 * name Object 
 * email Object 
 * password Object 
 * slackname Object 
 * researchgate Object 
 * defaultAppID Object 
 * defaultAppDescription Object 
 * no response value expected for this operation
 **/
exports.execute_signupPOST = function(avatar,name,email,password,slackname,researchgate,defaultAppID,defaultAppDescription) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Load login payload as group member for existing AI service agent
 *
 * id Object 
 * inviteremail Object  (optional)
 * inviterDefaultAppId Object  (optional)
 * inviterUserRole Object  (optional)
 * no response value expected for this operation
 **/
exports.load_loginPOST = function(id,inviteremail,inviterDefaultAppId,inviterUserRole) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Get member's profile and voting preferences of AI service agent
 *
 * id Object 
 * no response value expected for this operation
 **/
exports.load_members_profilePOST = function(id) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Load sign-up application payload as group member for new AI service agent
 *
 * id Object 
 * inviteremail Object  (optional)
 * no response value expected for this operation
 **/
exports.load_signupPOST = function(id,inviteremail) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}


/**
 * Get workgroup for AI service agent
 *
 * id Object 
 * defaultAppID Object 
 * no response value expected for this operation
 **/
exports.load_workgroupPOST = function(id,defaultAppID) {
  return new Promise(function(resolve, reject) {
    resolve();
  });
}

