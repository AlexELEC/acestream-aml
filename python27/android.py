# Copyright (C) 2009 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not
# use this file except in compliance with the License. You may obtain a copy of
# the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import os
import subprocess
import hashlib

# Disk info
df = subprocess.Popen(["df", "/"], stdout=subprocess.PIPE)
output = df.communicate()[0]
disk_device, disk_size, disk_used, disk_available, disk_percent, disk_mountpoint = output.split("\n")[1].split()
# Memory info
free = subprocess.Popen(["free", "-b"], stdout=subprocess.PIPE)
output = free.communicate()[0]
mem_mem, mem_total, mem_used, mem_free, mem_shared, mem_buffers, mem_cached = output.split("\n")[1].split()

class Android(object):
  def __init__(self,addr=None):
    self.onEPGUpdated = None
    self.onPlaylistUpdated = None

  @staticmethod
  def getAceStreamHome():
    return os.path.abspath(os.curdir)

  @staticmethod
  def makeToast(msg):
    print msg

  @staticmethod
  def getDeviceName():
    return "Amlogic"

  @staticmethod
  def getDeviceModel():
     return os.uname()[0]

  @staticmethod
  def getDeviceProductName():
    return "Amlogic"

  @staticmethod
  def getDeviceManufacturer():
    return "Amlogic"

  @staticmethod
  def getAppId():
    return hashlib.sha1("acestream")

  @staticmethod
  def getAppVersionCode():
    return "3014400"

  @staticmethod
  def getDisplayLanguage():
    return "ru_RU"

  @staticmethod
  def getRAMSize():
    return int(mem_total)

  @staticmethod
  def getTotalMemory():
    return int(mem_total)

  @staticmethod
  def getMaxMemory():
    return int(mem_cached)

  @staticmethod
  def getMemoryClass():
    return 16

  @staticmethod
  def getDeviceId():
    return hashlib.sha1("AMLBOX")

  @staticmethod
  def onSettingsUpdated():
    return None

  @staticmethod
  def getBlockSize(self):
    return 1024

  @staticmethod
  def getBlockCount(self):
    return int(disk_size) # in blocksize

  @staticmethod
  def getAvailableBlocks(self):
    return int(disk_available) # in blocksize

  @staticmethod
  def getRAMSize():
    return int(mem_total)
