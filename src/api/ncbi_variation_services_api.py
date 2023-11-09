# Citation: NHI Variation Services: https://api.ncbi.nlm.nih.gov/variation/v0/

# Packages imported
import requests
import json

# TODO: test the error message output. see if its informative enough
# TODO: rewrite documentation for this function because the error message has changed.


class VarServAPI:
    def __init__(self) -> None:
        """Initialize class with the API URL"""

        self.base_ncbi_url_api = "https://api.ncbi.nlm.nih.gov/variation/v0/"

        self.headers = {"Content-Type": "application/json; charset=utf-8"}

    def _spdi_attribute_concat(self, r: requests.Response) -> str:
        """Extract SPDI attributes, and concatenating the attributes to create a SPDI expression.

        Args:
            r (request.Response): The response containing SPDI data.

        Raises:
            requests.HTTPError: If the request fails with a non-200 status code.

        Returns:
            str: A SPDI expression
        """

        response_json = json.loads(r.text)
        try:
            spdi_dict = response_json["data"]["spdis"][0]
        except KeyError:
            raise requests.HTTPError(
                f"Failed to extract SPDI attributes from response: {response_json}"
            )
        return ":".join(
            (
                spdi_dict["seq_id"],
                # NOTE: The position is an integer in response but is converted into a string in order to join the attributes.
                str(spdi_dict["position"]),
                spdi_dict["deleted_sequence"],
                spdi_dict["inserted_sequence"],
            )
        )


    def validate_spdi(self, spdi_id: str) -> str:
        """
        Validates the given SPDI expression and returns the corresponding SPDI expression.

        Args:
            spdi_id (str): The SPDI expression to validate.

        Raises:
            requests.HTTPError: If the request to the NCBI Variation Services API fails.
            requests.HTTPError: If the response from the NCBI Variation Services API indicates an error.

        Returns:
            str: The validated SPDI expression in the format "seq_id:position:deleted_sequence:inserted_sequence".
        """

        endpoint = "/spdi/{}/".format(spdi_id)
        url = f"{self.base_ncbi_url_api}{endpoint}"
        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            response_json = json.loads(response.text)
            spdi_dict = response_json["data"]
            return ":".join(
                (
                    spdi_dict["seq_id"],
                    str(spdi_dict["position"]),
                    spdi_dict["deleted_sequence"],
                    spdi_dict["inserted_sequence"],
                )
            )
        else:
            try:
                error_json = response.json()
                error_message = error_json.get("error", {}).get(
                    "message", "Unknown error"
                )
                raise requests.HTTPError(
                    f"Failed to validate SPDI expression: {spdi_id}. Error message: {error_message}"
                )
            except json.JSONDecodeError:
                raise requests.HTTPError(
                    f"Failed to parse error response as JSON: {response.text}"
                )

    def spdi_to_hgvs(self, spdi_id: str) -> str:
            """
            Converts an SPDI expression to right-shift HGVS expression. End point used from NCBI variation services api: /spdi/{spdi}/hgvs

            Args:
                spdi_id (str): The SPDI expression to convert.

            Raises:
                requests.HTTPError: If there was an error with the HTTP request.
                requests.HTTPError: If there was an error converting the SPDI expression to HGVS expression.

            Returns:
                str: The Right shift normalized HGVS expression for the given SPDI expression.
            """
            endpoint = "/spdi/{}/hgvs".format(spdi_id)

            url = f"{self.base_ncbi_url_api}{endpoint}"

            response = requests.get(url, headers=self.headers)

            if response.status_code == 200:
                return json.loads(response.text)["data"]["hgvs"]
            else:
                try:
                    error_json = response.json()
                    error_message = error_json["error"]["message"]
                    raise requests.HTTPError(
                        f"Failed to convert SPDI expression {spdi_id} to HGVS notation. Error message: {error_message}"
                    )
                except json.JSONDecodeError:
                    raise requests.HTTPError(
                        f"Failed to parse error response as JSON: {response.text}"
                    )

    def hgvs_to_spdi(self, hgvs_id: str, assembly: str = "GCF_000001405.38") -> str:
        """
        Converts an HGVS expression to SPDI expression. End point used from NCBI variation service api: /hgvs/{hgvs}/contextuals

        Args:
            hgvs_id (str): The HGVS expression to convert.
            assembly (str, optional): The genome assembly. Defaults to "GCF_000001405.38".

        Raises:
            requests.HTTPError: If there was an error converting the HGVS expression to SPDI expression.

        Returns:
            str: The SPDI expression for the given HGVS expression.
        """
        
        endpoint = "/hgvs/{}/contextuals{}".format(hgvs_id, assembly)

        url = f"{self.base_ncbi_url_api}{endpoint}"

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            return self._spdi_attribute_concat(response)
        else:
            try:
                error_json = response.json()
                error_message = error_json.get("error", {}).get(
                    "message", "Unknown error"
                )
                raise requests.HTTPError(
                    f"Failed to convert HGVS expression {hgvs_id} to SPDI notation. Error message: {error_message}"
                )
            except json.JSONDecodeError:
                raise requests.HTTPError(
                    f"Failed to parse error response as JSON: {response.text}"
                )

