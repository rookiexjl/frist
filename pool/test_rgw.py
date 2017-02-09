#!/usr/bin/env python

import logging
from pool import rgwget


logging.basicConfig(level=logging.WARNING)


#     def setUp(self):
#         self.rgwget = rgwadmin.RGWAdmin(secure=False, verify=False, **get_environment_creds())
#         self.user1 = 'foo1209'
#         self.user2 = 'foo1213'
#         self.user3 = 'bar3142'
#         self.secret = rgwadmin.RGWAdmin.gen_secret_key()
#         user1 = self.rgwget.create_user(uid=self.user1,
#                                      email='%s@example.com' % self.user1,
#                                      display_name='Unit Test %s' % self.user1,
#                                      secret_key=self.secret)
#         user2 = self.rgwget.create_user(uid=self.user2,
#                                      display_name='Unit Test %s' % self.user2,
#                                      secret_key=self.secret)
#         self.user1_obj = user1
#         self.user2_obj = user2
#         self.assertTrue(user1['user_id'] == self.user1)
#         self.assertTrue(user2['user_id'] == self.user2)
# 
#     def tearDown(self):
#         self.rgwget.remove_user(uid=self.user1)
#         self.rgwget.remove_user(uid=self.user2)
# 
#     def test_modify_user(self):
#         user = self.rgwget.modify_user(uid=self.user1,
#                                     email='%s@test.com' % self.user1)
#         self.assertTrue(user['email'] == '%s@test.com' % self.user1)
# 
#     def test_duplicate_email(self):
#         with self.assertRaises(EmailExists):
#             self.rgwget.create_user(uid=self.user3,
#                                  email='%s@example.com' % self.user1,
#                                  display_name='Unit Test %s' % self.user3,
#                                  secret_key=rgwadmin.RGWAdmin.gen_secret_key())
# 
#     def test_get_user(self):
#         user = self.rgwget.get_user(uid=self.user2)
#         self.assertTrue(user['display_name'] == 'Unit Test %s' % self.user2)

def test_get_users():
    users = rgwget.RGWAdmin.get_users()
    print users

#     def test_user_quota(self):
#         size = random.randint(1000, 1000000)
#         self.rgwget.set_quota(uid=self.user1, quota_type='user',
#                            max_size_kb=size, enabled=True)
#         user1_quota_info = self.rgwget.get_user_quota(uid=self.user1)
#         self.assertTrue(size == user1_quota_info['max_size_kb'])
# 
#     def test_bucket(self):
#         bucket_name = self.user1 + '_bucket'
#         self.rgwget.create_bucket(bucket=bucket_name)
#         bucket = self.rgwget.get_bucket(bucket=bucket_name)
#         self.rgwget.link_bucket(bucket=bucket_name, bucket_id=bucket['id'],
#                              uid=self.user1)
#         self.rgwget.get_bucket(uid=self.user1, bucket=bucket_name)
#         self.rgwget.get_policy(bucket=bucket_name)
#         self.rgwget.remove_bucket(bucket=bucket_name, purge_objects=True)
#         self.assertTrue(True)
# 
#     def test_get_usage(self):
#         summary = self.rgwget.get_usage(show_summary=True)
#         self.assertTrue('summary' in summary)
# 
#     def test_subuser(self):
#         self.rgwget.create_subuser(uid=self.user2,
#                                 subuser='swift',
#                                 key_type='swift',
#                                 secret_key=self.secret)
#         self.rgwget.modify_subuser(uid=self.user2,
#                                 subuser='swift',
#                                 access='write')
#         subuser = self.rgwget.get_user(uid=self.user2)
#         self.rgwget.remove_subuser(uid=self.user2, subuser='swift')
#         for subs in subuser['subusers']:
#             if subs['id'] == '%s:%s' % (self.user2, 'swift'):
#                 self.assertTrue(subs['permissions'] == 'write')
# 
#     def test_s3_keys(self):
#         access = rgwadmin.RGWAdmin.gen_secret_key(size=20)
#         secret = rgwadmin.RGWAdmin.gen_secret_key(size=40)
#         keys = self.rgwget.create_key(uid=self.user1,
#                                    access_key=access,
#                                    secret_key=secret)
#         for key in keys:
#             if key['access_key'] == access:
#                 self.assertTrue(key['secret_key'] == secret)



if __name__ == '__main__':
    test_get_users()
