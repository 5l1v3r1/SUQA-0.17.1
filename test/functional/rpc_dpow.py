#!/usr/bin/env python2
# Copyright (c) 2018 The Hush developers
# Distributed under the MIT software license, see the accompanying
# file COPYING or http://www.opensource.org/licenses/mit-license.php.

from test_framework.test_framework import BitcoinTestFramework
from test_framework.util import assert_equal, initialize_datadir

class DPoWTest(BitcoinTestFramework):
    def set_test_params(self):
        self.setup_clean_chain = False
        self.num_nodes = 1

    def run_test(self):
        self.nodes[0].generate(3)
        rpc = self.nodes[0]

        result = rpc.getinfo()
        print(result)
        # regtest should have no notarization data, this test makes sure we do not see mainnet values as well!
        assert_equal(result['notarized'],0)
        assert_equal(result['notarizedhash'],'0000000000000000000000000000000000000000000000000000000000000000')
        assert_equal(result['notarizedtxid'],'0000000000000000000000000000000000000000000000000000000000000000')

if __name__ == '__main__':
    DPoWTest().main()
