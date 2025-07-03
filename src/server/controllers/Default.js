'use strict';

var utils = require('../utils/writer.js');
var Default = require('../service/DefaultService');

module.exports.execute_loginPOST = function execute_loginPOST (req, res, next) {
  var name = req.swagger.params['name'].value;
  var password = req.swagger.params['password'].value;
  var inviterDefaultAppId = req.swagger.params['inviterDefaultAppId'].value;
  var inviterUserRole = req.swagger.params['inviterUserRole'].value;
  Default.execute_loginPOST(name,password,inviterDefaultAppId,inviterUserRole)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.execute_logoutPOST = function execute_logoutPOST (req, res, next) {
  Default.execute_logoutPOST()
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.execute_signupPOST = function execute_signupPOST (req, res, next) {
  var avatar = req.swagger.params['avatar'].value;
  var name = req.swagger.params['name'].value;
  var email = req.swagger.params['email'].value;
  var password = req.swagger.params['password'].value;
  var slackname = req.swagger.params['slackname'].value;
  var researchgate = req.swagger.params['researchgate'].value;
  var defaultAppID = req.swagger.params['defaultAppID'].value;
  var defaultAppDescription = req.swagger.params['defaultAppDescription'].value;
  Default.execute_signupPOST(avatar,name,email,password,slackname,researchgate,defaultAppID,defaultAppDescription)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.load_loginPOST = function load_loginPOST (req, res, next) {
  var id = req.swagger.params['id'].value;
  var inviteremail = req.swagger.params['inviteremail'].value;
  var inviterDefaultAppId = req.swagger.params['inviterDefaultAppId'].value;
  var inviterUserRole = req.swagger.params['inviterUserRole'].value;
  Default.load_loginPOST(id,inviteremail,inviterDefaultAppId,inviterUserRole)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.load_members_profilePOST = function load_members_profilePOST (req, res, next) {
  var id = req.swagger.params['id'].value;
  Default.load_members_profilePOST(id)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.load_signupPOST = function load_signupPOST (req, res, next) {
  var id = req.swagger.params['id'].value;
  var inviteremail = req.swagger.params['inviteremail'].value;
  Default.load_signupPOST(id,inviteremail)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};

module.exports.load_workgroupPOST = function load_workgroupPOST (req, res, next) {
  var id = req.swagger.params['id'].value;
  var defaultAppID = req.swagger.params['defaultAppID'].value;
  Default.load_workgroupPOST(id,defaultAppID)
    .then(function (response) {
      utils.writeJson(res, response);
    })
    .catch(function (response) {
      utils.writeJson(res, response);
    });
};
