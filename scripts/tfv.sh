for i in $(jq -r ".resources[].instances" /home/ubuntu/oci_provision/terraform.tfstate)
do
	echo $i >> ~/tf.txt
done
