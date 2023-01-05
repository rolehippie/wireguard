# wireguard

[![Source Code](https://img.shields.io/badge/github-source%20code-blue?logo=github&logoColor=white)](https://github.com/rolehippie/wireguard) [![General Workflow](https://github.com/rolehippie/wireguard/actions/workflows/general.yml/badge.svg)](https://github.com/rolehippie/wireguard/actions/workflows/general.yml) [![Readme Workflow](https://github.com/rolehippie/wireguard/actions/workflows/readme.yml/badge.svg)](https://github.com/rolehippie/wireguard/actions/workflows/readme.yml) [![Galaxy Workflow](https://github.com/rolehippie/wireguard/actions/workflows/galaxy.yml/badge.svg)](https://github.com/rolehippie/wireguard/actions/workflows/galaxy.yml) [![License: Apache-2.0](https://img.shields.io/github/license/rolehippie/wireguard)](https://github.com/rolehippie/wireguard/blob/master/LICENSE) [![Ansible Role](https://img.shields.io/ansible/role/51444)](https://galaxy.ansible.com/rolehippie/wireguard)

Ansible role to install and configure wireguard VPN.

## Sponsor

Building and improving this Ansible role have been sponsored by my current and previous employers like **[Cloudpunks GmbH](https://cloudpunks.de)** and **[Proact Deutschland GmbH](https://www.proact.eu)**.

## Table of content

- [Default Variables](#default-variables)
  - [wireguard_interface](#wireguard_interface)
  - [wireguard_ip](#wireguard_ip)
  - [wireguard_netmask](#wireguard_netmask)
  - [wireguard_peers](#wireguard_peers)
  - [wireguard_port](#wireguard_port)
  - [wireguard_private](#wireguard_private)
  - [wireguard_public](#wireguard_public)
- [Discovered Tags](#discovered-tags)
- [Dependencies](#dependencies)
- [License](#license)
- [Author](#author)

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

## Discovered Tags

**_wireguard_**


## Dependencies

- None

## License

Apache-2.0

## Author

[Thomas Boerger](https://github.com/tboerger)
