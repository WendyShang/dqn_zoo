# Copyright 2019 DeepMind Technologies Limited. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
"""Tests for Rainbow."""

# pylint: disable=g-bad-import-order

from absl import flags
from absl.testing import flagsaver

from dqn_zoo.rainbow_flare import run_atari
from absl.testing import absltest

FLAGS = flags.FLAGS


class RunAtariFlareTest(absltest.TestCase):

  @flagsaver.flagsaver
  def test_can_run_agent(self):
    FLAGS.environment_name = 'pong'
    FLAGS.replay_capacity = 1000
    FLAGS.target_network_update_period = 3
    FLAGS.num_train_frames = 100
    FLAGS.num_eval_frames = 50
    FLAGS.num_iterations = 3
    FLAGS.batch_size = 10
    FLAGS.learn_period = 2
    run_atari.main(None)


if __name__ == '__main__':
  absltest.main()
