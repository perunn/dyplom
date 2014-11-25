__author__ = 'perun'

import core.calculations as calc


class Circuit:
    def __init__(self, intensity=None, index=None, loss=0.002):

        """


        :param intensity: Intensity which network generate to the core
        :param index: Index of the network
        :param loss: The probability of losing call. Need for the calculation of the network resources
        """
        # Values into the gateway from the network
        self.intensity_voice_in = intensity
        self.links_in = 0
        self.pcm_in = 0
        self.r_in = 0
        self.dsp_in = 0
        self.flow_voice_in = 0
        self.flow_voice_in_list = []

        # Values out of the gateway to the network
        self.intensity_voice_out = 0
        self.links_out = 0
        self.pcm_out = 0
        self.r_out = 0
        self.dsp_out = 0
        self.flow_voice_out = 0

        # General values
        self.interest_row_voice = []
        self.interest_row_video = []
        self.interest_row_be = []
        self.index = index
        self.name = "PSTN/ISDN/GSM " + str(index)
        self.loss = loss

        # Variables connected with codec
        self.lambda_g711 = 100
        self.lambda_g729 = 100

        # Protocols' heading load: 40[B], length of voice sample with g711 = 80B, total length of single package is
        # 50[B] = 8*120 [b] = 1060
        self.package_length_g711 = 960

        # Protocols' heading load: 40[B], length of voice sample with g729 = 10B, total length of single package is
        # 50[B] = 8*50 [b] = 400
        self.package_length_g729 = 400

    def input_resources(self):
        """
        Method is calculating input (to the core network) resources on the edge of the network. It's using methods from
        calculation module.
        """
        self.links_in = calc.erlang_first_formula(self.intensity_voice_in, self.loss)
        self.pcm_in = calc.pcm_lines(self.links_in)
        self.r_in = calc.real_links(self.pcm_in)
        self.dsp_in = calc.dsp(self.r_in)

    def set_flow_voice_in(self, networks=None):

        for net in networks:

            if 'GSM' in net.name:
                tmp = (self.interest_row_voice[net.index] *
                       self.r_in *
                       self.lambda_g711 *
                       self.package_length_g711)

                self.flow_voice_in += tmp
            else:
                tmp = (self.interest_row_voice[net.index] *
                       self.r_in *
                       self.lambda_g729 *
                       self.package_length_g729)
                self.flow_voice_in += tmp

            self.flow_voice_in_list.append(tmp)

    def set_flow_voice_out(self, networks=None):

        for net in networks:
                self.flow_voice_out += net.flow_voice_in_list[self.index]

    def output_resources(self):
        """
        Method is calculating output (from the core network) resources on the edge of the network. It's using methods
        from calculation module.
        """
        self.links_out = calc.erlang_first_formula(self.intensity_voice_out, self.loss)
        self.pcm_out = calc.pcm_lines(self.links_out)
        self.r_out = calc.real_links(self.pcm_out)
        self.dsp_out = calc.dsp(self.r_out)

    def reset_resources(self):

        #Values out of the gateway to the network
        """

        Method reset calculated values
        """

        self.intensity_voice_out = 0
        self.links_out = 0
        self.pcm_out = 0
        self.r_out = 0
        self.dsp_out = 0
        self.flow_voice_out = 0

    def set_intensity_voice_out(self, networks=None):
        """
        Method is counting the output intensity of the network.
        :param networks: list of all created networks in the core
        """
        for x in networks:
            self.intensity_voice_out += x.intensity_voice_in*x.interest_row_voice[self.index]

    def set_index(self, index):
        self.index = index
        self.set_name()

    def set_name(self):
        self.name = "PSTN/ISDN/GSM " + str(self.index)


class Package:
    def __init__(self, intensity_voice=0, index=None, intensity_video=0, intensity_mail=0):

        """

        :param intensity_voice: Intensity which network generate to the core
        :param index: Index of the network
        """
        #Values into the core network from access network
        self.intensity_voice_in = intensity_voice
        self.intensity_video_in = intensity_video
        self.intensity_be_in = intensity_mail

        #Variables describing flow out the IP network for different types of traffic
        self.flow_voice_in = 0
        self.flow_video_in = 0
        self.flow_be_in = 0
        #this value is used to process with Circuit networks
        self.intensity_in = self.intensity_voice_in/100

        #Values from the core network to the access network
        self.intensity_voice_out = 0
        self.intensity_video_out = 0
        self.intensity_be_out = 0

        self.intensity_out = 0

        #Variables describing flow into the IP network for different types of traffic
        self.flow_voice_out = 0
        self.flow_video_out = 0
        self.flow_be_out = 0

        #General values
        self.interest_row_voice = []
        self.interest_row_video = []
        self.interest_row_be = []
        self.index = index
        self.name = "Dostęp IP " + str(index)
        self.loss = 0

        # Protocols' heading load: 40[B], length of voice sample with g711 = 80B, total length of single package is
        # 50[B] = 8*120 [b] = 1060
        self.package_length_g711 = 960

        # Protocols' heading load: 40[B], length of voice sample with g729 = 10B, total length of single package is
        # 50[B] = 8*50 [b] = 400
        self.package_length_g729 = 400

    def reset_resources(self):

        #Values from the core network to the access network
        self.intensity_out = 0

        self.flow_voice_in = 0
        self.flow_video_in = 0
        self.flow_be_in = 0

        self.intensity_voice_out = 0
        self.intensity_video_out = 0
        self.intensity_be_out = 0

        self.flow_voice_out = 0
        self.flow_video_out = 0
        self.flow_be_out = 0

    def set_intensity_voice_in(self, n):
        self.intensity_voice_in = n
        self.intensity_in = self.intensity_voice_in/100

    def set_index(self, index):
        self.index = index
        self.set_name()

    def set_name(self):
        self.name = "Dostęp IP " + str(self.index)

    def out_intensity(self):
        pass