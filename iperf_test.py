from parser import parse_client_output

class TestSuite():
    def test_iperf_client_connection(self, server, client):
        transfer_threshold=0.125
        bandwidth_treshold=0.625

        server_error = server
        result, error = client
        assert not error
        assert not server_error
        
        intervals = parse_client_output(result)
        for interval in intervals:
            transfer = float(interval["Transfer"])
            bandwidth = float(interval["Bandwidth"])
            assert transfer >= transfer_threshold
            assert bandwidth >= bandwidth_treshold