# wireguard

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/wireguard) [![Build Status](https://img.shields.io/drone/build/rolehippie/wireguard/master?logo=drone)](https://cloud.drone.io/rolehippie/wireguard) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/wireguard)](https://github.com/rolehippie/wireguard/blob/master/LICENSE) 

Ansible role to install and configure wireguard VPN. 

## Sponsor 

[![Proact Deutschland GmbH](https://proact.eu/wp-content/uploads/2020/03/proact-logo.png)](https://proact.eu) 

Building and improving this Ansible role have been sponsored by my employer **Proact Deutschland GmbH**.

## Table of content

* [Default Variables](#default-variables)
  * [wireguard_interface](#wireguard_interface)
  * [wireguard_ip](#wireguard_ip)
  * [wireguard_netmask](#wireguard_netmask)
  * [wireguard_peers](#wireguard_peers)
  * [wireguard_port](#wireguard_port)
  * [wireguard_private](#wireguard_private)
  * [wireguard_public](#wireguard_public)
* [Dependencies](#dependencies)
* [License](#license)
* [Author](#author)

---

## Default Variables

### wireguard_interface

Interface to define

#### Default value

```YAML
wireguard_interface: wg0
```

### wireguard_ip

IP address of the wireguard node

#### Default value

```YAML
wireguard_ip:
```

### wireguard_netmask

Netmask of the wireguard node

#### Default value

```YAML
wireguard_netmask: 32
```

### wireguard_peers

List of peers to connect to

#### Default value

```YAML
wireguard_peers: []
```

### wireguard_port

Port to bind to

#### Default value

```YAML
wireguard_port: 51820
```

### wireguard_private

Private encryption key

#### Default value

```YAML
wireguard_private:
```

### wireguard_public

Public encryption key

#### Default value

```YAML
wireguard_public:
```

## Dependencies

* None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
