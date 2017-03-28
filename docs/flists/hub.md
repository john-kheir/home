# Hub

The hub is active on `http://hub.gig.tech`


## Installation

All the code for the Hub can be found on https://github.com/g8os/hub

The README explains how to deploy your own instance.

- You need to create ItsYou.online API key in order to have client secret
- Don't forget to set callback url, including `_iyo_callback`
- Compile a Caddy with the OAuth plugin for ItsYou.online OAuth, available from https://github.com/itsyouonline/caddy-integration
- Install JumpScale from the correct branch: `8.2.0`, this version contains all dependencies needed by flist, used on the Hub, including the g8storclient
- You will need to deploy a ARDB instance for the storage, make it read-write (no special configuration) and not exposed publicly, no specific backend is required, RocksDB is a good choice
  - Expose this ARDB instance  as `PRIVATE_ARDB_` in the config
- A front Redis (in slave-of mode, read-only by default) needs to run, exposed publicly
  - Expose this Redis instance as `PUBLIC_ARDB_` in the config


## Testing

To make sure everything works:

- You should be able to access the Hub front page, click on the `Upload my files` button, and able to login with ItsYou.online
- On the upload page, you should see your username in the top right corner
- Create a small `.tar.gz` file with anything you want on it, and upload it
- The summary page should appear with all links working properly
